#!/usr/bin/env python

from PyQt4 import QtGui, QtCore
from interface import *
from song import *

class interface(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(interface, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.connect(self.ui.actionEsci_2, QtCore.SIGNAL("activated()"), self.exit_called)

    def exit_called(self):
        print "TODO: Save data on exit"

if __name__ == "__main__":
    app = QtGui.QApplication(None)
    widget = interface()
    widget.show()
    app.exec_()
