
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_index import Ui_index


class MyWindow(QWidget, Ui_index):

    diasCnt = 2

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self._init_main_window()  # 主窗口初始化设置

    def _init_main_window(self):
        # 设置窗体无边框
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # 设置背景透明
        # self.setAttribute(Qt.WA_TranslucentBackground)
        pass
    def addDialog(self,text,mode='robert'):
        try:
            print('adding')
            self.diasCnt += 1
            _translate = QtCore.QCoreApplication.translate
            robert = QtWidgets.QFrame(self.scrollAreaWidgetContents)
            robert.setGeometry(QtCore.QRect(0, self.diasCnt*58, 760, 58))
            robert.setFrameShape(QtWidgets.QFrame.StyledPanel)
            robert.setFrameShadow(QtWidgets.QFrame.Raised)
            robert.setObjectName("dia_"+str(self.diasCnt))
            horizontalLayout_2 = QtWidgets.QHBoxLayout(robert)
            horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
            if mode=='robert':
                horizontalLayout_2.setContentsMargins(25, 5, 0, 5)
            else:
                horizontalLayout_2.setContentsMargins(0, 5, 25, 5)
            horizontalLayout_2.setSpacing(16)
            horizontalLayout_2.setObjectName("horizontalLayout_"+str(self.diasCnt))
            robertImg = QtWidgets.QLabel(robert)
            robertImg.setMinimumSize(QtCore.QSize(48, 48))
            robertImg.setMaximumSize(QtCore.QSize(48, 48))
            robertImg.setStyleSheet("border-radius: 24px;\n"
                                         "background-color: #fff;")
            robertImg.setText("")
            robertImg.setObjectName("robertImg_"+str(self.diasCnt))

            horizontalLayout_2.addWidget(robertImg)
            robertText = QtWidgets.QLabel(robert)
            robertText.setEnabled(True)
            robertText.setStyleSheet("background-color: #ffffff;\n"
                                          "border-radius: 12px;\n"
                                          "padding:4px")
            robertText.setFrameShape(QtWidgets.QFrame.Box)
            robertText.setFrameShadow(QtWidgets.QFrame.Plain)
            robertText.setObjectName("robertText_"+str(self.diasCnt))
            robertText.setText(_translate("index", text))

            # self.scrollAreaWidgetContents.layout.addWidget(robert)
            self.verticalLayout.addWidget(robert)

        except Exception as e:
            print(e)

    def test(self):
        try:
            text = QtWidgets.QLabel('Text')
            self.layout().addWidget(text)
            print(type(self.right))
        except Exception as e:
            print(e)




def main():

    # 创建QApplication类的实例
    app = QApplication(sys.argv)
    # form = QWidget()
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':

    main()
