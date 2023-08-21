from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from ui.theme import style
from components.terminal import Term
import sys

class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.adjustUi()

    def setupUi(self):
        self.centralFrame = QFrame()
        self.Layout = QVBoxLayout(self.centralFrame)
        self.centralFrame.setLayout(self.Layout)
        self.setCentralWidget(self.centralFrame)
        
        self.Terminal = Term()
        self.Layout.addWidget(self.Terminal)

    def adjustUi(self):
        self.setWindowTitle("73r-")
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet(style)
        self.resize(500, 500)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    instance = Game()
    instance.show()
    sys.exit(app.exec())