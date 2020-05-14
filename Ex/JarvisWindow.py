# Downloaded modules
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit, \
    QLabel, QTextEdit, QFrame, QTableWidget, QMainWindow, QTableWidgetItem, QDialogButtonBox
from PyQt5 import QtCore
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.patches as patches

# Local imports
from Geo_Algorithms import GeoAlgorithms
from random import randint


class JarvisWin(QWidget):
    def __init__(self):
        super().__init__()

        self.row_cnt = 50
        self.col_cnt = 2

        self.initUI()

    def initUI(self):

        self.grid = QGridLayout()

        self.grid.addWidget(self.pointsTable(), 0, 0)
        self.grid.addWidget(self.butGo(), 1, 0, alignment=QtCore.Qt.AlignCenter)
        self.grid.addWidget(self.butClear(), 2, 0, alignment=QtCore.Qt.AlignCenter)
        self.grid.addWidget(self.graphLabel(), 0, 1)

        self.setLayout(self.grid)

        self.setGeometry(200, 200, 900, 500)
        self.setObjectName("jarvis")
        self.setWindowTitle('Jarvis Algorithm')
        self.setStyleSheet('''
        #jarvis {
            background: #002f1f;
        }
        ''')
        self.show()

    def pointsTable(self):
        self.table = QTableWidget()
        self.table.setColumnCount(self.col_cnt)
        self.table.setRowCount(self.row_cnt)
        self.table.setHorizontalHeaderLabels(["X", "Y"])
        for i in range(self.row_cnt):
            for j in range(self.col_cnt):
                self.table.setItem(i, j, QTableWidgetItem(""))
        col = self.table.horizontalHeader()
        row = self.table.verticalHeader()
        for i in range(self.col_cnt):
            col.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        for i in range(self.row_cnt):
            row.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        self.table.setMaximumHeight(480)

        return self.table

    def graphLabel(self, pic="./pics/graph.png"):
        self.l = QLabel()
        pixmap = QtGui.QPixmap(pic)
        self.l.setPixmap(pixmap)

        return self.l

    def butGo(self):
        but = QPushButton()
        but.setText("Go!")
        but.clicked.connect(self.drawGraph)
        but.setFixedSize(150, 30)

        return but

    def butClear(self):
        but = QPushButton()
        but.setText("Clear table")
        but.clicked.connect(self.clearTable)
        but.setFixedSize(150, 30)

        return but

    def drawGraph(self):
        data = []
        for i in range(self.row_cnt):
            x, y = (0, 0)
            try:
                x = int(self.table.item(i, 0).text())
                y = int(self.table.item(i, 1).text())
                data.append([x, y])
            except:
                pass
        fig = plt.figure()
        ax = fig.add_subplot(111, aspect='equal')
        try:
            points = GeoAlgorithms.Jarvis_March(data)
        except:
            return
        x, y = (0, 0)
        for i in range(len(points)):
            points[i] = (float(points[i][0]), float(points[i][1]))
            x = points[i][0] if points[i][0] > x else x
            y = points[i][1] if points[i][1] > y else y
        ax.add_patch(patches.Polygon(xy=points, fill=False))
        ax.plot(x + 2, y + 2)
        pic_id = randint(1, 1243545)
        path = "./pics/Jarvis#{}.png".format(pic_id)
        plt.savefig(path)
        self.layout().itemAt(3).widget().setParent(None)
        self.grid.addWidget(self.graphLabel(path), 0, 1)

    def clearTable(self):
        for i in range(self.row_cnt):
            for j in range(self.col_cnt):
                self.table.item(i, j).setText("")