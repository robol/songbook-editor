# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'options.ui'
#
# Created: Fri May 15 17:06:57 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_options(object):
    def setupUi(self, options):
        options.setObjectName("options")
        options.resize(400, 266)
        self.buttonBox = QtGui.QDialogButtonBox(options)
        self.buttonBox.setGeometry(QtCore.QRect(30, 210, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtGui.QWidget(options)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 50, 341, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.paper_size = QtGui.QComboBox(self.gridLayoutWidget)
        self.paper_size.setObjectName("paper_size")
        self.paper_size.addItem(QtCore.QString())
        self.paper_size.addItem(QtCore.QString())
        self.gridLayout.addWidget(self.paper_size, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.type = QtGui.QComboBox(self.gridLayoutWidget)
        self.type.setObjectName("type")
        self.type.addItem(QtCore.QString())
        self.type.addItem(QtCore.QString())
        self.type.addItem(QtCore.QString())
        self.gridLayout.addWidget(self.type, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.title = QtGui.QLineEdit(self.gridLayoutWidget)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.subtitle = QtGui.QLineEdit(self.gridLayoutWidget)
        self.subtitle.setObjectName("subtitle")
        self.gridLayout.addWidget(self.subtitle, 3, 1, 1, 1)
        self.label = QtGui.QLabel(options)
        self.label.setGeometry(QtCore.QRect(160, 20, 141, 16))
        self.label.setObjectName("label")

        self.retranslateUi(options)
        QtCore.QMetaObject.connectSlotsByName(options)

    def retranslateUi(self, options):
        options.setWindowTitle(QtGui.QApplication.translate("options", "Opzioni LaTeX", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("options", "Formato", None, QtGui.QApplication.UnicodeUTF8))
        self.paper_size.setItemText(0, QtGui.QApplication.translate("options", "A4 (290mm x 210mm)", None, QtGui.QApplication.UnicodeUTF8))
        self.paper_size.setItemText(1, QtGui.QApplication.translate("options", "A5 (210mm x 145mm)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("options", "Tipo di Canzoniere", None, QtGui.QApplication.UnicodeUTF8))
        self.type.setItemText(0, QtGui.QApplication.translate("options", "Testo e accordi", None, QtGui.QApplication.UnicodeUTF8))
        self.type.setItemText(1, QtGui.QApplication.translate("options", "Solo Testo", None, QtGui.QApplication.UnicodeUTF8))
        self.type.setItemText(2, QtGui.QApplication.translate("options", "Slide", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("options", "Titolo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("options", "Sottotitolo", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("options", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Opzioni LaTex</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

