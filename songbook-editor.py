#!/usr/bin/env python

from PyQt4 import QtGui, QtCore
from interface import *
from song import *
from latex_manager import *
import re

class interface(QtGui.QMainWindow):
    def __init__(self, lm, parent=None):
        super(interface, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Create an empty database of songs... 
        self.song_db = []

        # Connections
        self.connect(self.ui.actionEsci_2, QtCore.SIGNAL("activated()"), self.exit_called)
        self.connect(self.ui.btn_create_latex_song, QtCore.SIGNAL("clicked()"), self.create_latex_song)
        self.connect(self.ui.btn_savesong, QtCore.SIGNAL("clicked()"), self.savesong)
        self.connect(self.ui.list_songs, QtCore.SIGNAL("currentTextChanged ( QString )"), self.item_selected)
        self.connect(self.ui.btn_new_song, QtCore.SIGNAL("clicked()"), self.new_song)
    
    # Functions to manage events
    def new_song(self):
        s = song("")
        self.set_active_song(s)
    

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
    
        
    def item_selected(self, item_text):
        print "ohi"
        for song in self.song_db:
            if(song.title == unicode(item_text)):
                newsong = song
        self.set_active_song(newsong)


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
    app = QtGui.QApplication(None)
    lm = latex_manager()
    widget = interface(lm)
    widget.show()
    app.exec_()
