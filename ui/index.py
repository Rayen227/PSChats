import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtUiTools import QUiLoader
from PyQt5.QtWidgets import QApplication, QWidget
import resource_rc


class CommonHelper:
    def __init__(self):
        pass

    @staticmethod
    def readQss(style):
        with open(style, 'r') as f:
            return f.read()

# 动态载入


class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # PySide2
        self.ui = QUiLoader().load('index.ui')

        # styleFile = 'index.qss'
        # qssStyle = CommonHelper.readQss(styleFile)
        # self.setStyleSheet(qssStyle)
        # 这里与静态载入不同，使用 self.ui.show()
        # 如果使用 self.show(),会产生一个空白的 MainWindow
        self.ui.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainwindow()
    sys.exit(app.exec_())
