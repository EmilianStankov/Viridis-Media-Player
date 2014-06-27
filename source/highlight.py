from PyQt4 import QtGui
from PyQt4 import QtCore


class Highlighter(QtGui.QTextEdit):
    def __init__(self, text, pattern):
        super(Highlighter, self).__init__()

        self.text = text
        self.setText(self.text)
        cursor = self.textCursor()

        format = QtGui.QTextCharFormat()
        format.setBackground(QtGui.QBrush(QtGui.QColor("green")))

        self.pattern = pattern
        regex = QtCore.QRegExp(pattern)

        pos = 0
        index = regex.indexIn(self.toPlainText(), pos)
        while (index != -1):
            cursor.setPosition(index)
            cursor.movePosition(QtGui.QTextCursor.EndOfLine, 1)
            cursor.mergeCharFormat(format)
            pos = index + regex.matchedLength()
            index = regex.indexIn(self.toPlainText(), pos)
