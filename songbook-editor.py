#!/usr/bin/env python

import re,sys, os
sys.path.append("./libs")
sys.path.append("./ui")
# Questo e' solo un trucchetto per fare in modo che il programm
# trovi le mie librerie anche se viene lanciato da strani posti :)
os.chdir("".join(sys.argv[0].rsplit("songbook-editor.py",1)))
from PyQt4 import QtGui, QtCore
from interface import *
from options import *
from song import *
from latex_manager import *



class interface(QtGui.QMainWindow):
    def __init__(self, lm, parent=None):
        super(interface, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # options Database
        self.opt = {}
        self.set_default_options()

        # Create an empty database of songs... 
        self.song_db = []

        # Our format separator
        self.sep = ":::"
        self.sep_song = "***"

        # Song edit part
        self.connect(self.ui.btn_create_pdf, QtCore.SIGNAL("clicked()"), self.export_to_PDF)
        self.connect(self.ui.btn_savesong, QtCore.SIGNAL("clicked()"), self.savesong)

        # About the list
        self.connect(self.ui.list_songs, QtCore.SIGNAL("currentTextChanged ( QString )"), self.item_selected)
        self.connect(self.ui.btn_new_song, QtCore.SIGNAL("clicked()"), self.new_song)
        self.connect(self.ui.btn_delete_song, QtCore.SIGNAL("clicked()"), self.delete_item_from_list)
        self.connect(self.ui.btn_list_move_down, QtCore.SIGNAL("clicked()"), self.list_move_down)
        self.connect(self.ui.btn_list_move_up, QtCore.SIGNAL("clicked()"), self.list_move_up)

        # Menu File
        self.connect(self.ui.actionSalva, QtCore.SIGNAL("activated()"), self.save_songbook)
        self.connect(self.ui.actionApri, QtCore.SIGNAL("activated()"), self.load_songbook)

        # Menu Canzone
        self.connect(self.ui.actionSalva_canzone, QtCore.SIGNAL("activated()"), self.save_song_to_file)
        self.connect(self.ui.actionImporta_canzone, QtCore.SIGNAL("activated()"), self.import_song_from_file)
        self.connect(self.ui.actionEsporta_in_DVI, QtCore.SIGNAL("activated()"), self.export_to_DVI)
        self.connect(self.ui.actionEsporta_in_PDF, QtCore.SIGNAL("activated()"), self.export_to_PDF)

        # Menu Canzoniere
        self.connect(self.ui.actionEsporta_in_LaTeX, QtCore.SIGNAL("activated()"), self.export_songbook)
        self.connect(self.ui.actionOpzioni_LaTeX, QtCore.SIGNAL("activated()"), self.options)
    
    # Functions to manage events

    # Reset the song screen on right and start working on a new song
    def new_song(self):
        s = song("")
        self.set_active_song(s)

    # Delete the selected song from the list AND from the song_db
    def delete_item_from_list(self):
        song = self.get_active_song()
        item = self.ui.list_songs.currentRow()
        self.ui.list_songs.takeItem(item)
        self.song_db.remove(song)

    # Get the song object of the active song
    def get_active_song(self):
        # Get data
        newtitle = unicode(self.ui.le_title.text())
        newmauthor = unicode(self.ui.le_mauthor.text())
        newtauthor = unicode(self.ui.le_tauthor.text())
        newyear = unicode(self.ui.le_year.text())
        newtone = unicode(self.ui.le_tone.text())
        newsong = song(newtitle, [], newmauthor, newtauthor, newtone, newyear)

        newbody = unicode(self.ui.te_body.toPlainText())
        # Just debug
        # print newbody
        newbody = re.split("\n\n+", newbody)
        for paragraph in newbody:
            if(len(paragraph) < 3):
                break
            if( (paragraph[0] == 'R') & (paragraph[1] == ':') ):
                newsong.add_chorus(paragraph.split("R:")[1])
            else:
                newsong.add_verse(paragraph)

        return newsong

    def get_active_song_in_list(self):
        newsong = self.get_active_song()
        for song in self.song_db:
            if( (song.title == newsong.title) ):
                return song

    # Add a new song in the db, and update the list
    def add_song_to_db(self, song):
        self.song_db.append(song)
        self.list_update()

    # Save (and eventually overwrite) the active song in the songbook
    def savesong(self):
        need_new_song = True
        song_to_save = self.get_active_song()
        list_item = QtGui.QListWidgetItem(song_to_save.title)
        # Check if we have already saved this song or if it's a new entry
        for song in self.song_db:
            if(song.title == song_to_save.title):
                # Questa linea di codice e' orribile, ma non capisco come dovrei fare per salvare la canzone
                self.song_db[self.song_db.index(song)] = song_to_save 
                need_new_song = False
                break            
        if(need_new_song):
            self.add_song_to_db(song_to_save)

    def get_item_from_song(self, song):
        self.list_update()
        ind = self.song_db.index(song)
        return self.ui.list_songs.item(ind)

    def list_move_up(self):
        song = self.get_active_song_in_list()
        ind = self.song_db.index(song)
        if(ind == 0):
            return
        self.song_db.pop(ind)
        self.song_db.insert(ind-1, song)
        self.list_update()
        self.ui.list_songs.setItemSelected(self.get_item_from_song(song), 1)

    def list_move_down(self):
        song = self.get_active_song_in_list()
        ind = self.song_db.index(song)
        if(ind == len(self.song_db)):
            return
        self.song_db.pop(ind)
        self.song_db.insert(ind+1, song)
        self.list_update()
        self.ui.list_songs.setItemSelected(self.get_item_from_song(song), 1)



    # Export song to a rcs file
    def save_song_to_file(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, "Salva Canzone", "", "Canzoni di RobolCanzoniere (*.rcs)")
        output = self.create_song_file()
        handle = open(filename, 'w')
        handle.write(output.encode("utf-8"))
        handle.close()

    # Export songbook to a rcc file
    def save_songbook(self):
        # Default format is concatenated song files, with self.song_sep to
        # separate them, so
        saving = ""
        for song in self.song_db:
            saving += self.create_song_file(song) + self.sep_song
        filename = QtGui.QFileDialog.getSaveFileName(self, "Salva Canzoniere", "", "Canzoniere di RobolCanzoniere (*.rcc)")
        if(filename != ""):
            handle = open(filename, 'w')
            handle.write(saving.encode("utf-8"))
            handle.close()

    # Load songbook from a rcc file
    def load_songbook(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, "Apri Canzoniere", "", "Canzoniere di RobolCanzoniere (*.rcc)")
        if(filename != ""):
            handle = open(filename, 'r')
            buf = handle.read().decode("utf-8")
            handle.close()
        else:
            return
        song_list = buf.split(self.sep_song)
        self.song_db = []
        for raw_song in song_list:
            if(raw_song != ""):
                self.add_song_to_db(self.file_to_song(raw_song))
        # Update the list view
        # self.list_update() This is not necessary anymore, because of
        # the add_song_to_db function managing the widget update :)
        # Less fast, but more readable!


    # Update the list view. This function is used from all the other functions that
    # edit the self.song_db to make the list widget respecting it
    def list_update(self):
        self.ui.list_songs.clear()
        for song in self.song_db:
            self.ui.list_songs.addItem(song.title)
            

    # Create the rcs file of song_to_save (non interactive function) that returns it
    def create_song_file(self, song_to_save=''):
        sep = unicode(self.sep)
        if(song_to_save == ''):
            song_to_save = self.get_active_song()
        # filename = QtGui.QFileDialog.getSaveFileName(self, "Salva canzone", "", "Canzoni di RobolCanzoniere (*.rcs)")
        # handle = open(filename, 'w')
        output = unicode()
        output += song_to_save.title + sep + song_to_save.mauthor + sep + song_to_save.tauthor + sep + song_to_save.tone + sep + song_to_save.year
        for par in song_to_save.body:
            if(par.is_chorus()):
                rit = "R:"
            else:
                rit = ""
            output += sep + rit + par.content()
        return output

    # Convert a file (rcs) to a song object
    def file_to_song(self, file_content):
        buf = file_content.split(self.sep)
        newsong = song(buf[0], [], buf[1], buf[2], buf[3], buf[4])
        for j in range(5,1024):
            try:
                if( (buf[j][0] == 'R') & (buf[j][1] == ':') ):
                    newsong.add_chorus(buf[j].split("R:")[1])
                else:
                    newsong.add_verse(buf[j])
            except:
                break
        return newsong
            
    # import a song from a file on the local hard drive, the function is interactive!    
    def import_song_from_file(self):
        filetoimport = QtGui.QFileDialog.getOpenFileName(self, "Importa canzone", "", "Canzoni di RobolCanzoniere (*.rcs)")
        handle = open(filetoimport, 'r')
        buf = handle.read().decode("utf-8")
        handle.close()
        self.set_active_song(self.file_to_song(buf))

    def set_active_song(self, newsong):
        self.ui.le_title.setText(newsong.title)
        self.ui.le_mauthor.setText(newsong.mauthor)
        self.ui.le_tauthor.setText(newsong.tauthor)
        self.ui.le_year.setText(newsong.year)
        self.ui.le_tone.setText(newsong.tone)
        output = unicode()
        for paragraph in newsong.body:
            if(paragraph.is_chorus()):
                output += "R:"
            output += paragraph.content()
            output += "\n\n"
        self.ui.te_body.setDocument(QtGui.QTextDocument(output, self.ui.te_body))
    
        
    def item_selected(self, item_text):
        newsong = ""
        for song in self.song_db:
            if(song.title == unicode(item_text)):
                newsong = song
        if(newsong!=""):
            self.set_active_song(newsong)
        else:
            self.new_song

    # Converte una canzone in un file LaTeX non autosufficiente, che puo' essere inserito in un altro canzoniere latex.
    def create_latex_song(self):
        song = self.get_active_song()
        filetowrite = lm.create_song(song)
        filename = QtGui.QFileDialog.getSaveFileName(self, "Salva file latex", "/home/leonardo", "LaTeX Source File (*.tex)")
        if(filename == ''):
            # We do not have to do nothing, the user clicked Cancel
            return 0
        handle = open(filename, 'w')
        # Just remember that filetowrite is an "unicode" object, treat it
        # as it just deserve
        handle.write(filetowrite.encode("utf-8"))
        handle.close()


    # Esporta il canzoniere in LaTeX, in ogni caso dovra' essere esportato
    def export_songbook(self):
        # Chiedo al latex manager di farlo.. :)
        sbk = lm.export_songbook(self.song_db, widget.opt)

        # Apriamo un file
        filename = QtGui.QFileDialog.getSaveFileName(self, "Salva file latex", "/home/leonardo", "LaTeX Source File (*.tex)")
        if(filename == ''):
            # We do not have to do nothing, the user clicked Cancel
            return 0
        handle = open(filename, 'w')
        handle.write(sbk.encode("utf-8"))
        handle.close()

    # Esporta il canzoniere in DVI
    def export_to_DVI(self):
        # Otteniamo il codice LaTeX
        sbk = lm.export_songbook(self.song_db, widget.opt) 
        # Compiliamo il DVI
        dvifile = lm.latex_compile(sbk, widget.opt)
        # Apriamo un file                                                                                                                                                          
        filename = QtGui.QFileDialog.getSaveFileName(self, "Salva file DVI", "", "DVI file (*.dvi)")
        if(filename == ''):
            # We do not have to do nothing, the user clicked Cancel                                                                                                                
                return 0
        handle = open(filename, 'wb')
        handle.write(dvifile)
        handle.close()

    # Esporta il canzoniere in PDF
    def export_to_PDF(self):
        pdf_file = lm.create_pdf_from_songbook(self.song_db, widget.opt)
        # Apriamo un file                                                                                                                                                          
        filename = QtGui.QFileDialog.getSaveFileName(self, "Salva file PDF", "", "PDF file (*.pdf)")
        if(filename == ''):
            # We do not have to do nothing, the user clicked Cancel                                                                                                                
            return 0
        handle = open(filename, 'wb')
        handle.write(pdf_file)
        handle.close()

        

    def options(self):
        # self.opt = option_interface()
        option.show()

    def set_default_options(self):
        self.opt["paper_size"] = "A5"
        self.opt["title"] = "Canzoniere"
        self.opt["subtitle"] = "Autore Sconosciuto"
        self.opt["type"] = "tc" ## tc = text and chords, c = only chords, s = slide


# This class manage the Dialog that prompt the user for
# common options...
class option_interface(QtGui.QWidget):
    def __init__(self, parent=None):
        super(option_interface,self).__init__(parent)
        self.ui = Ui_options()
        self.ui.setupUi(self)

        # Options dictionary
        self.paper_size_dic = {"A4":1, "A5":2}
        

        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.ok)
        self.connect(self.ui.buttonBox, QtCore.SIGNAL("rejected()"), self.cancel)

    def cancel(self):
        self.hide()

    def ok(self):
        # Set paper size
        if(self.ui.paper_size.currentIndex() == 1):
            widget.opt["paper_size"] = "A4"
        elif(self.ui.paper_size.currentIndex() == 2):
            widget.opt["paper_size"] = "A5"

        # Set songbook type
        if(self.ui.type.currentIndex() == 1):
            widget.opt["type"] = "tc"
        elif(self.ui.type.currentIndex() == 2):
            widget.opt["type"] = "c"
        elif(self.ui.type.currentIndex() == 3):
            widget.opt["type"] == "s"
        
        # Set songbook title
        widget.opt["title"] = unicode(self.ui.title.text())
        # Set songbook subtitle
        widget.opt["subtitle"] = unicode(self.ui.subtitle.text())
        
        # Hide options
        self.hide()
            


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    option = option_interface()
    lm = latex_manager()
    widget = interface(lm)
    widget.show()
    app.exec_()
