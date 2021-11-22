import sys
from scripts import  index
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui= index.MainWindowController(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
