import sys
import random
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.bull = False

    def run(self):
        self.update()

    def xs(self, x):
        return x + 200 // 2

    def ys(self, y):
        return 200 // 2 - y

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):
        qp.setBrush(Qt.yellow)
        a = random.randint(50, 300)
        qp.drawEllipse(50, 50, a, a)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
