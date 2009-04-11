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

        # Connections
        self.connect(self.ui.actionEsci_2, QtCore.SIGNAL("activated()"), self.exit_called)
        self.connect(self.ui.btn_create_latex_song, QtCore.SIGNAL("clicked()"), self.create_latex_song)

    # Functions to manage events
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
