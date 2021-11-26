import sys
from utils import audioManager
from utils import api
from PyQt5.Qt import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication
from ui import main
from nn import NN
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process,Pool
from PySide2.QtUiTools import QUiLoader

import datetime


class Main():

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.mainWindow = main.MyWindow()
        self.mainWindow.show()

        self.microphoneClickCnt = 0
        self.hitory = []
        self.curMsg = {}
        self.model = NN()
        self.ar = None
        self.pool = ThreadPoolExecutor(max_workers=3)
        self.__eventsBinding()

        sys.exit(self.app.exec_())

    def __eventsBinding(self):
        # 发送点击事件
        self.mainWindow.kp_if_w_send.clicked.connect(self.__sendText)
        # 麦克风点击事件
        self.mainWindow.kp_if_microphone.clicked.connect(self.__microphoneClicked)
        pass


    def __sendText(self):
        text = self.mainWindow.kp_if_w_sendEdit.toPlainText()
        if text == "":
            return
        self.curMsg = {
            'time':datetime.date.today(),
            'input':text,
            'output':'',
            'status':100,
        }
        curI = len(self.hitory)
        self.hitory.append(self.curMsg)
        self.mainWindow.kp_if_w_sendEdit.setText('')
        self.mainWindow.addUserDialog(text=text)

        future = self.pool.submit(self.model.test,text)
        def __callback(res):
            print(res.result())
            self.hitory[curI]['status']=200
            self.hitory[curI]['output']=res.result()
            print(self.hitory)
        future.add_done_callback(__callback)

    def __recordEndCallback(self):
        print('__recordEndCallback')
        # self.mainWindow.addUserDialog('')
        # def __test():
        #     sleep(3)
        #     return 'test end'
        # # future = self.pool.submit(api.speech_to_text_baidu,'cache/cache01.wav',False)
        #
        # future = self.pool.submit(__test)
        # def __callback(res):
        #     # print(res.result())
        #     self.mainWindow.addRobertDialog(res.result())
        # future.add_done_callback(__callback)


    def __microphoneClicked(self):

        self.microphoneClickCnt += 1


        if(self.microphoneClickCnt % 2 == 1):

            print('Recording ...')
            if self.ar is not None : del self.ar
            self.ar = audioManager.AudioRecorder()
            self.ar.setCallback(self.__recordEndCallback)
            self.ar.start()
        else:
            self.ar.stopRecord()
            print('Recorded')


    def __recordEnd(self):
        # if (self.ar is not None):
        #     self.ar.stopRecord()
            # self.ap.start()
        pass

    # 文字转语音
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



