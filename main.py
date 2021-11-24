import sys
from utils import audioManager
from utils import api
from PyQt5.Qt import QApplication
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader


class Main():

    def __init__(self):
        self.app = QApplication(sys.argv)
        # self.MainWindow = QMainWindow()
        self.ui = QUiLoader().load('ui/index.ui')
        self.ui.show()
        # self.ar = audioManager.AudioRecorder()
        self.ap = audioManager.AudioPlayer()

        # self.ui.setupUi(self.MainWindow)
        # self.MainWindow.show()

        self.__eventsBinding()

        sys.exit(self.app.exec_())

    def __eventsBinding(self):
        # self.ui.pushButton_1.clicked.connect(self.__recordStart)
        # self.ui.pushButton_2.clicked.connect(self.__recordEnd)
        # self.ui.pushButton_3.clicked.connect(self.__saySentence)
        pass



    def __recordStart(self):
        # if (self.ar is None):
        self.ar = audioManager.AudioRecorder(lambda :print('callback'))
        self.ar.start()

    def __recordEnd(self):
        if (self.ar is not None):
            self.ar.stopRecord()
            self.ap.start()

    def __saySentence(self):
        api.text_to_speech('哈哈哈哈哈哈哈哈哈哈哈')





if __name__ == '__main__':
    test = Main()

    # res = api.speech_to_text_baidu(if_microphone=True)
    # res = api.speech_to_text_baidu('cache/test.wav', if_microphone=False)
    # res = api.speech_to_text_cmu('cache/test.wav', if_microphone=False)
    # print(res)
    # MainWindow.show()
    # obtain audio from the microphone


    # 测试数据库链接
    # dbm = dbmanager.DBManager()
    # # res = dbm.addUser('2111220001','test01','男')
    # res = dbm.selectAllUser()
    # print(res.content.decode('utf-8'))

    # 测试音频输入输出
    # am = audioManager.AutoAudioManager()
    # am.start()
    # am.record_audio('cache/test.wav',5)
    # am.play_audio('cache/test.wav')



