# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created: Sat Jun 20 17:44:08 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 781, 541))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.list_songs = QtGui.QListWidget(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_songs.sizePolicy().hasHeightForWidth())
        self.list_songs.setSizePolicy(sizePolicy)
        self.list_songs.setObjectName("list_songs")
        self.gridLayout.addWidget(self.list_songs, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_delete_song = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_delete_song.sizePolicy().hasHeightForWidth())
        self.btn_delete_song.setSizePolicy(sizePolicy)
        self.btn_delete_song.setObjectName("btn_delete_song")
        self.horizontalLayout.addWidget(self.btn_delete_song)
        self.btn_list_move_up = QtGui.QPushButton(self.gridLayoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/images/up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_list_move_up.setIcon(icon)
        self.btn_list_move_up.setObjectName("btn_list_move_up")
        self.horizontalLayout.addWidget(self.btn_list_move_up)
        self.btn_list_move_down = QtGui.QPushButton(self.gridLayoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/images/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_list_move_down.setIcon(icon1)
        self.btn_list_move_down.setObjectName("btn_list_move_down")
        self.horizontalLayout.addWidget(self.btn_list_move_down)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 2, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.le_title = QtGui.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_title.sizePolicy().hasHeightForWidth())
        self.le_title.setSizePolicy(sizePolicy)
        self.le_title.setObjectName("le_title")
        self.gridLayout_2.addWidget(self.le_title, 0, 1, 1, 1)
        self.le_tauthor = QtGui.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_tauthor.sizePolicy().hasHeightForWidth())
        self.le_tauthor.setSizePolicy(sizePolicy)
        self.le_tauthor.setObjectName("le_tauthor")
        self.gridLayout_2.addWidget(self.le_tauthor, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.le_mauthor = QtGui.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_mauthor.sizePolicy().hasHeightForWidth())
        self.le_mauthor.setSizePolicy(sizePolicy)
        self.le_mauthor.setObjectName("le_mauthor")
        self.gridLayout_2.addWidget(self.le_mauthor, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.le_year = QtGui.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_year.sizePolicy().hasHeightForWidth())
        self.le_year.setSizePolicy(sizePolicy)
        self.le_year.setObjectName("le_year")
        self.gridLayout_2.addWidget(self.le_year, 3, 1, 1, 1)
        self.le_tone = QtGui.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_tone.sizePolicy().hasHeightForWidth())
        self.le_tone.setSizePolicy(sizePolicy)
        self.le_tone.setObjectName("le_tone")
        self.gridLayout_2.addWidget(self.le_tone, 4, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.te_body = QtGui.QTextEdit(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.te_body.sizePolicy().hasHeightForWidth())
        self.te_body.setSizePolicy(sizePolicy)
        self.te_body.setAcceptRichText(False)
        self.te_body.setObjectName("te_body")
        self.verticalLayout.addWidget(self.te_body)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_savesong = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_savesong.sizePolicy().hasHeightForWidth())
        self.btn_savesong.setSizePolicy(sizePolicy)
        self.btn_savesong.setObjectName("btn_savesong")
        self.horizontalLayout_2.addWidget(self.btn_savesong)
        self.btn_new_song = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_new_song.sizePolicy().hasHeightForWidth())
        self.btn_new_song.setSizePolicy(sizePolicy)
        self.btn_new_song.setObjectName("btn_new_song")
        self.horizontalLayout_2.addWidget(self.btn_new_song)
        self.btn_create_pdf = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_create_pdf.sizePolicy().hasHeightForWidth())
        self.btn_create_pdf.setSizePolicy(sizePolicy)
        self.btn_create_pdf.setObjectName("btn_create_pdf")
        self.horizontalLayout_2.addWidget(self.btn_create_pdf)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 2, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuCanzoniere = QtGui.QMenu(self.menubar)
        self.menuCanzoniere.setObjectName("menuCanzoniere")
        self.menuCanzone = QtGui.QMenu(self.menubar)
        self.menuCanzone.setObjectName("menuCanzone")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionApri = QtGui.QAction(MainWindow)
        self.actionApri.setObjectName("actionApri")
        self.actionEsci = QtGui.QAction(MainWindow)
        self.actionEsci.setObjectName("actionEsci")
        self.actionSalva = QtGui.QAction(MainWindow)
        self.actionSalva.setObjectName("actionSalva")
        self.actionEsci_2 = QtGui.QAction(MainWindow)
        self.actionEsci_2.setObjectName("actionEsci_2")
        self.actionSalva_canzone = QtGui.QAction(MainWindow)
        self.actionSalva_canzone.setObjectName("actionSalva_canzone")
        self.actionImporta_canzone = QtGui.QAction(MainWindow)
        self.actionImporta_canzone.setObjectName("actionImporta_canzone")
        self.actionEsporta_in_LaTeX = QtGui.QAction(MainWindow)
        self.actionEsporta_in_LaTeX.setObjectName("actionEsporta_in_LaTeX")
        self.actionOpzioni_LaTeX = QtGui.QAction(MainWindow)
        self.actionOpzioni_LaTeX.setObjectName("actionOpzioni_LaTeX")
        self.actionEsporta_in_DVI = QtGui.QAction(MainWindow)
        self.actionEsporta_in_DVI.setObjectName("actionEsporta_in_DVI")
        self.actionEsporta_in_PDF = QtGui.QAction(MainWindow)
        self.actionEsporta_in_PDF.setObjectName("actionEsporta_in_PDF")
        self.menuFile.addAction(self.actionApri)
        self.menuFile.addAction(self.actionSalva)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionEsci_2)
        self.menuCanzoniere.addAction(self.actionEsporta_in_LaTeX)
        self.menuCanzoniere.addAction(self.actionOpzioni_LaTeX)
        self.menuCanzoniere.addAction(self.actionEsporta_in_DVI)
        self.menuCanzoniere.addAction(self.actionEsporta_in_PDF)
        self.menuCanzone.addAction(self.actionSalva_canzone)
        self.menuCanzone.addAction(self.actionImporta_canzone)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuCanzoniere.menuAction())
        self.menubar.addAction(self.menuCanzone.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionEsci_2, QtCore.SIGNAL("activated()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "SongBook Editor 0.2", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_delete_song.setText(QtGui.QApplication.translate("MainWindow", "Elimina Canzone", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Titolo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Autore", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Copyright", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Anno", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Tonalità", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_savesong.setText(QtGui.QApplication.translate("MainWindow", "Aggiungi al canzoniere", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_new_song.setText(QtGui.QApplication.translate("MainWindow", "Nuova Canzone", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_create_pdf.setText(QtGui.QApplication.translate("MainWindow", "Esporta canzoniere in PDF", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Lista Canzoni</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Canzone selezionata</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCanzoniere.setTitle(QtGui.QApplication.translate("MainWindow", "Canzoniere", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCanzone.setTitle(QtGui.QApplication.translate("MainWindow", "Canzone", None, QtGui.QApplication.UnicodeUTF8))
        self.actionApri.setText(QtGui.QApplication.translate("MainWindow", "Apri", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEsci.setText(QtGui.QApplication.translate("MainWindow", "Esci", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalva.setText(QtGui.QApplication.translate("MainWindow", "Salva", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEsci_2.setText(QtGui.QApplication.translate("MainWindow", "Esci", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalva_canzone.setText(QtGui.QApplication.translate("MainWindow", "Salva canzone", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImporta_canzone.setText(QtGui.QApplication.translate("MainWindow", "Importa canzone", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEsporta_in_LaTeX.setText(QtGui.QApplication.translate("MainWindow", "Esporta in LaTeX", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpzioni_LaTeX.setText(QtGui.QApplication.translate("MainWindow", "Opzioni LaTeX", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEsporta_in_DVI.setText(QtGui.QApplication.translate("MainWindow", "Esporta in DVI", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEsporta_in_PDF.setText(QtGui.QApplication.translate("MainWindow", "Esporta in PDF", None, QtGui.QApplication.UnicodeUTF8))

