import sys
from ui import ui_index
import time
from scripts import audioManager
from db import dbmanager
from PyQt5.Qt import QWidget, QApplication, QMainWindow, QThread, QMutex, pyqtSignal


# aam = audioManager.AutoAudioManager()

# class MainThread(QThread):
#     def __init__(self):
#         super().__init__()
#
#     def run(self):
#         cnt=0
#         while(True):
#             print(cnt)
#             cnt+=1
#             time.sleep(0.5)

class Main():

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.MainWindow = QMainWindow()
        self.ui = ui_index.Ui_MainWindow()
        self.aam = None

        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

        self.__eventsBinding()

        sys.exit(self.app.exec_())

    def __eventsBinding(self):
        self.ui.pushButton.clicked.connect(self.__pushEvent)

    def __pushEvent(self):
        if (self.aam is not None):
            self.aam.stopRecord()


    def __recordStart(self):
        if (self.aam is None):
            self.aam = audioManager.AutoAudioManager()


if __name__ == '__main__':
    Main()
    # MainWindow.show()


    # 测试数据库链接
    # dbm = dbmanager.DBManager()
    # # res = dbm.addUser('2111220001','test01','男')
    # res = dbm.selectAllUser()
    # print(res.content.decode('utf-8'))

    # 测试音频输入输出
    # am = audioManager.AudioManager()
    # am.record_audio('cache/test.wav',5)
    # am.play_audio('cache/test.wav')
    # am.autoRecord()


