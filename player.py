import sys
from MainScreen import MainScreen
from PyQt4 import QtGui


def main():
    app = QtGui.QApplication(sys.argv)
    main_screen = MainScreen()
    main_screen.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
