from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys


class MyWindow(QMainWindow):
    """ designed for just showcase event in PyQt"""
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setGeometry(100, 100, 550, 200)
        self.setWindowTitle("Learn Event")
        self.setStyleSheet("background-color:yellow")

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label: ")
        self.label.setGeometry(50, 130, 200, 40)
        self.label.setStyleSheet("color:red")

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("click me!!")
        self.button.setGeometry(50, 50, 150, 50)
        self.button.setStyleSheet("background-color:orange")
        self.button.clicked.connect(self.click_fun)

    def click_fun(self):
        """ perform click event """
        self.label.setText("button pressed")
        self.update()

    def update(self):
        """ method to adjust text size after click """
        self.label.adjustSize()


def my_window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    my_window()

