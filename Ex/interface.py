# Standard library imports
import sys
from datetime import date

# Downloaded modules
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit, \
    QLabel, QTextEdit, QFrame, QTableWidget, QMainWindow, QTableWidgetItem, QDialogButtonBox
from PyQt5 import QtCore

# Local modules
from JarvisWindow import JarvisWin
from GrahamWindow import GrahamWin
from SequantialWindow import SequantialWin


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.grid = QGridLayout()

        self.grid.addWidget(self.butJarvis(), 0, 0)
        self.grid.addWidget(self.butGraham(), 0, 1)
        self.grid.addWidget(self.butSequantial(), 0, 2)


        self.setLayout(self.grid)

        self.setGeometry(100, 100, 700, 600)
        self.setWindowTitle('Geometrical Algorithms')
        self.setObjectName("bg")
        self.setStyleSheet('''
        #bg {
            background: #002f1f;
        }
        ''')
        self.show()

    def butJarvis(self):
        but = QPushButton()
        but.setText("Jarvis Algorithm")
        but.clicked.connect(self.openJarvisWindow)

        return but

    def butGraham(self):
        but = QPushButton()
        but.setText("Graham Algorithm")
        but.clicked.connect(self.openGrahamWindow)

        return but

    def butSequantial(self):
        but = QPushButton()
        but.setText("Sequantial Algorithm")
        but.clicked.connect(self.openSequantialWindow)

        return but

    def openJarvisWindow(self):
        self.jarvis = JarvisWin()

    def openGrahamWindow(self):
        self.graham = GrahamWin()

    def openSequantialWindow(self):
        self.seq = SequantialWin()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec())