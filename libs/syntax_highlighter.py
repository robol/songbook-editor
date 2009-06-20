from PyQt4 import QtGui

class syntax_highlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, parent):
        super(syntax_highlighter, self).__init__(parent)
        
    def highlightBlock(self, text):
        if(len(text) >= 2):
            if((text[0] == "R") & (text[1] == ":") ):
                self.setFormat(0, 2,QtGui.QColor(0,0,255))
        intag = False
        bold_font = QtGui.QTextCharFormat()
        bold_font.setFontWeight(QtGui.QFont.Bold)
        for i in range(0, len(text)):
            if(text[i] == "["):
                intag = True
                self.setFormat(i, 1, QtGui.QColor(255,0,255))
            elif(intag):
                self.setFormat(i, 1, QtGui.QColor(255,0,255))
                self.setFormat(i, 1, bold_font)
                if(text[i] == "]"):
                    intag = False
                    self.setFormat(i, 1, QtGui.QColor(255,0,255))


        


    
