from ui import index


class MainWindowController:

    def __init__(self,MainWindow):
        self.__ui = index.Ui_MainWindow()
        self.__ui.setupUi(MainWindow)
        # self.__ui.pushButton.keyPressEvent = self.__pushEvent
        self.__ui.pushButton.clicked.connect(self.__pushEvent)

    def getObject(self):
        return self.__ui

    def __pushEvent(self):
        self.__ui.label.setText("test02")
