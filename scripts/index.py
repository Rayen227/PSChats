from temporal import ui_index
from utils import audioManager
'''
MainWindowController: 主窗口控制工具
向前：获取、绑定、操作ui界面上数据
向后：包装、发起服务器请求、获取后台数据等
'''
class MainWindowController:

    def __init__(self,MainWindow):
        self.__ui = ui_index.Ui_MainWindow()
        self.__ui.setupUi(MainWindow)
        # self.__ui.pushButton.keyPressEvent = self.__pushEvent
        self.__ui.pushButton_1.clicked.connect(self.__pushEvent)
        MainWindow.show()
        self.__am = audioManager.AudioManager()
        self.__am.autoRecord()

    def getObject(self):
        return self.__ui

    def __pushEvent(self):
        self.__ui.label_1.setText("stop")
        self.__am.stopRecord()
