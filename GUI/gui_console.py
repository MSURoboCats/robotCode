from PyQt5.QtWidgets import QTextBrowser
from pyqt5_plugins.examplebuttonplugin import QtGui


class GUIConsole:

    def __init__(self, edit: QTextBrowser, out=None, color=None) -> None:
        self.edit = edit
        self.out = out
        self.color = color

    def write(self, m: str) -> None:
        if self.color:
            tc = self.edit.textColor()
            self.edit.setTextColor(self.color)

        self.edit.moveCursor(QtGui.QTextCursor.End)
        self.edit.insertPlainText(m)

        if self.color:
            self.edit.setTextColor(tc)

        if self.out:
            self.out.write(m)
