#!/usr/bin/env python

from PyQt4 import QtGui, QtCore
from interface import *
from song import *
from latex_manager import *
import re, sys

class interface(QtGui.QMainWindow):
    def __init__(self, lm, parent=None):
        super(interface, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Create an empty database of songs... 
        self.song_db = []

        # Our format separator
        self.sep = ":::"
        self.sep_song = "***"

        # Connections
        self.connect(self.ui.actionEsci_2, QtCore.SIGNAL("activated()"), self.exit_called)

        # Song edit part
        self.connect(self.ui.btn_create_latex_song, QtCore.SIGNAL("clicked()"), self.create_latex_song)
        self.connect(self.ui.btn_savesong, QtCore.SIGNAL("clicked()"), self.savesong)

        # About the list
        self.connect(self.ui.list_songs, QtCore.SIGNAL("currentTextChanged ( QString )"), self.item_selected)
        self.connect(self.ui.btn_new_song, QtCore.SIGNAL("clicked()"), self.new_song)
        self.connect(self.ui.btn_delete_song, QtCore.SIGNAL("clicked()"), self.delete_item_from_list)

        # File menu
        self.connect(self.ui.actionSalva_canzone, QtCore.SIGNAL("activated()"), self.save_song_to_file)
        self.connect(self.ui.actionImporta_canzone, QtCore.SIGNAL("activated()"), self.import_song_from_file)
        self.connect(self.ui.actionSalva, QtCore.SIGNAL("activated()"), self.save_songs_to_file)
    
    # Functions to manage events
    def new_song(self):
        s = song("")
        self.set_active_song(s)

    def delete_item_from_list(self):
        item = self.ui.list_songs.currentRow()
        self.ui.list_songs.takeItem(item)
    
    def exit_called(self):
        print "TODO: Save data on exit"

    def get_active_song(self):
        newtitle = unicode(self.ui.le_title.text())
        newmauthor = unicode(self.ui.le_mauthor.text())
        newtauthor = unicode(self.ui.le_tauthor.text())
        newyear = unicode(self.ui.le_year.text())
        newtone = unicode(self.ui.le_tone.text())
        newsong = song(newtitle, [], newmauthor, newtauthor, newtone, newyear)

        newbody = unicode(self.ui.te_body.toPlainText())
        print newbody
        newbody = re.split("\n\n+", newbody)
        for paragraph in newbody:
            if(len(paragraph) < 3):
                break
            if( (paragraph[0] == 'R') & (paragraph[1] == ':') ):
                newsong.add_chorus(paragraph.split("R:")[1])
            else:
                newsong.add_verse(paragraph)

        return newsong

    def savesong(self):
        need_new_song = True
        song_to_save = self.get_active_song()
        list_item = QtGui.QListWidgetItem(song_to_save.title)
        # Check if we have already saved this song or if it's a new entry
        for song in self.song_db:
            if(song.title == song_to_save.title):
                song = song_to_save
                need_new_song = False
                break
        if(need_new_song):
            self.song_db.append(song_to_save)
            self.ui.list_songs.addItem(list_item)

    def save_song_to_file(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, "Salva Canzone", "", "Canzoni di RobolCanzoniere (*.rcs)")
        output = self.create_song_file()
        handle = open(filename, 'w')
        handle.write(output.encode("utf-8"))
        handle.close()

    def create_song_file(self):
        sep = unicode(self.sep)
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
        # handle.write(output.encode())
        # handle.close()

    def save_songs_to_file(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, "Salva Canzoniere", "", "Canzoniere di RobolCanzoniere (*.rcc)")
        song_files = []
        for song in self.song_db:
            self.set_active_song(song)
            song_files.append(self.create_song_file)
        handle = open(filename, 'w')
        for song in song_files:
            handle.write((song + self.sep_song).encode("utf-8"))
        handle.close()
            
        

    def import_song_from_file(self):
        filetoimport = QtGui.QFileDialog.getOpenFileName(self, "Importa canzone", "", "Canzoni di RobolCanzoniere (*.rcs)")
        handle = open(filetoimport, 'r')
        buf = handle.read().decode("utf-8")
        handle.close()
        buf = buf.split(self.sep)
        newsong = song(buf[0], [], buf[1], buf[2], buf[3], buf[4])
        for j in range(5,1024):
            try:
                if( (buf[j][0] == 'R') & (buf[j][1] == ':') ):
                    newsong.add_chorus(buf[j].split("R:")[1])
                else:
                    newsong.add_verse(buf[j])
            except:
                break
        self.set_active_song(newsong)

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


    def create_latex_song(self):
        song = self.get_active_song()
        filetowrite = lm.create_song(song)
        filename = QtGui.QFileDialog.getSaveFileName(self, "Salva file latex", "/home/leonardo", "LaTeX Source File (*.tex)")
        handle = open(filename, 'w')
        # Just remember that filetowrite is an "unicode" object, treat it
        # as it just deserve
        handle.write(filetowrite.encode("utf-8"))
        handle.close()
    
    



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    lm = latex_manager()
    widget = interface(lm)
    widget.show()
    app.exec_()
