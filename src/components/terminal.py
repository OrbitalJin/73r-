from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class Term(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.setupAttrs()
        self.connectSignals()
        self.setObjectName("Terminal")

    def setupAttrs(self):
        self.History: list[str] = []
    
    def setupUi(self):
        self.Layout = QVBoxLayout(self)
        self.setLayout(self.Layout)

        self.Output = TermOut()
        
        self.Input = TermIn()
        self.Input.setFocus()
        self.Input.setFocusPolicy(Qt.StrongFocus)

        self.Layout.addWidget(self.Input)
        self.Layout.addWidget(self.Output)

    def connectSignals(self):
        self.Input.returnPressed.connect(self.cmdReturnedCallback)
        self.Input.textChanged.connect(self.textChangedCallback)

    def cmdReturnedCallback(self):
        cmd: str = self.Input.text()
        self.History.append(cmd)
        self.Input.clear()
        self.Output.add(cmd)


class TermOut(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.setObjectName("TermOut")

    def add(self, text: str):
        content: str = self.toPlainText()
        self.clear()
        cmd: str = "> " + text
        self.append(cmd)
        self.append(content)

class TermIn(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setObjectName("TermIn")
        self.setMinimumHeight(40)