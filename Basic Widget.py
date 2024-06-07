import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window():
    """ A simple application to create basic widget using PyQt """
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("Algomiz For Programming!!")

    label = QtWidgets.QLabel(win)
    label.setText("My First label: ")
    label.move(100, 50)

    # to show the window
    win.show()
    # Exit and close the application smoothly
    sys.exit(app.exec_())


if __name__ == "__main__":
    window()



