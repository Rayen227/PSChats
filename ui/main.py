
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_index import Ui_index


class MyWindow(QWidget, Ui_index):

    robertDiasCnt = 0
    userDiasCnt = 0

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self._init_main_window()  # 主窗口初始化设置
        self.__fill()

    def _init_main_window(self):
        # 设置窗体无边框
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # 设置背景透明
        # self.setAttribute(Qt.WA_TranslucentBackground)
        pass

    def __fill(self):
        self.addRobertDialog('你好呀，我是科科艾艾~懂得很多知识，欢迎你和我聊天噢！！',True)
        # self.addUserDialog('',False)
        # self.addRobertDialog('',False)
        # self.addUserDialog('',False)
        # self.addRobertDialog('',False)
        pass

    def addRobertDialog(self,text,visible=True):
        self.robertDiasCnt += 1 if visible else 0
        robert = QtWidgets.QFrame(
            self.kp_ca_scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            robert.sizePolicy().hasHeightForWidth())
        robert.setSizePolicy(sizePolicy)
        robert.setMaximumSize(QtCore.QSize(740, 16777215))
        robert.setFrameShape(QtWidgets.QFrame.StyledPanel)
        robert.setFrameShadow(QtWidgets.QFrame.Raised)
        robert.setObjectName("kp_ca_robert")
        horizontalLayout = QtWidgets.QHBoxLayout(robert)
        horizontalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        horizontalLayout.setContentsMargins(25, 5, 100, 5)
        horizontalLayout.setSpacing(16)
        horizontalLayout.setObjectName("horizontalLayout_"+str(self.robertDiasCnt))
        kp_ca_r_img = QtWidgets.QLabel(robert)
        kp_ca_r_img.setMinimumSize(QtCore.QSize(48, 48))
        kp_ca_r_img.setMaximumSize(QtCore.QSize(48, 48))
        kp_ca_r_img.setStyleSheet("border-radius: 24px;\n"
                                       "background-color: #fff;")
        kp_ca_r_img.setText("")
        kp_ca_r_img.setObjectName("kp_ca_r_img_"+str(self.robertDiasCnt))
        horizontalLayout.addWidget(kp_ca_r_img)
        kp_ca_r_text = QtWidgets.QLabel(text=text,parent=robert)
        kp_ca_r_text.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            kp_ca_r_text.sizePolicy().hasHeightForWidth())
        kp_ca_r_text.setSizePolicy(sizePolicy)
        kp_ca_r_text.setMaximumSize(QtCore.QSize(16777215, 16777215))
        kp_ca_r_text.setStyleSheet("background-color: #ffffff;\n"
                                        "border-radius: 12px;\n"
                                        "padding:4px")
        kp_ca_r_text.setFrameShape(QtWidgets.QFrame.Box)
        kp_ca_r_text.setFrameShadow(QtWidgets.QFrame.Plain)
        kp_ca_r_text.setTextFormat(QtCore.Qt.RichText)
        kp_ca_r_text.setObjectName("kp_ca_r_text_"+str(self.robertDiasCnt))
        horizontalLayout.addWidget(kp_ca_r_text)
        spacerItem = QtWidgets.QSpacerItem(
            700, 48, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontalLayout.addItem(spacerItem)
        horizontalLayout.setStretch(0, 80)
        robert.setVisible(visible)
        # robert.setO
        self.verticalLayout.addWidget(robert)
        self.kp_chatArea.verticalScrollBar().setValue((self.userDiasCnt + self.robertDiasCnt - 4) * 80)


    def addUserDialog(self,text,visible=True):
        try:
            self.userDiasCnt += 1 if visible else 0
            user = QtWidgets.QFrame(self.kp_ca_scrollAreaWidgetContents)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(user.sizePolicy().hasHeightForWidth())
            user.setSizePolicy(sizePolicy)
            user.setMaximumSize(QtCore.QSize(740, 16777215))
            user.setLayoutDirection(QtCore.Qt.RightToLeft)
            user.setFrameShape(QtWidgets.QFrame.StyledPanel)
            user.setFrameShadow(QtWidgets.QFrame.Raised)
            user.setObjectName("kp_ca_myUser_"+str(self.userDiasCnt))
            horizontalLayout = QtWidgets.QHBoxLayout(user)
            horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
            horizontalLayout.setContentsMargins(100, 5, 25, 5)
            horizontalLayout.setSpacing(16)
            horizontalLayout.setObjectName("horizontalLayout_"+str(self.userDiasCnt))
            kp_ca_mu_img = QtWidgets.QLabel(user)
            kp_ca_mu_img.setMinimumSize(QtCore.QSize(48, 48))
            kp_ca_mu_img.setMaximumSize(QtCore.QSize(48, 48))
            kp_ca_mu_img.setStyleSheet("border-radius: 24px;\n"
                                            "background-color: #fff;")
            kp_ca_mu_img.setText("")
            kp_ca_mu_img.setObjectName("kp_ca_mu_img_"+str(self.userDiasCnt))
            horizontalLayout.addWidget(kp_ca_mu_img)
            kp_ca_mu_text = QtWidgets.QLabel(text=text,parent=user)
            kp_ca_mu_text.setEnabled(True)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(kp_ca_mu_text.sizePolicy().hasHeightForWidth())
            kp_ca_mu_text.setSizePolicy(sizePolicy)
            kp_ca_mu_text.setMaximumSize(QtCore.QSize(16777215, 16777215))
            kp_ca_mu_text.setLayoutDirection(QtCore.Qt.RightToLeft)
            kp_ca_mu_text.setStyleSheet("background-color: #93D2FF;\n"
                                             "    border-radius: 12px;\n"
                                             "    padding:4px")
            kp_ca_mu_text.setInputMethodHints(QtCore.Qt.ImhNone)
            kp_ca_mu_text.setFrameShape(QtWidgets.QFrame.NoFrame)
            kp_ca_mu_text.setFrameShadow(QtWidgets.QFrame.Plain)
            kp_ca_mu_text.setObjectName("kp_ca_mu_text_"+str(self.userDiasCnt))
            horizontalLayout.addWidget(kp_ca_mu_text)
            spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            horizontalLayout.addItem(spacerItem)
            horizontalLayout.setStretch(0, 80)
            user.setVisible(visible)
            self.verticalLayout.addWidget(user)
            # self.kp_ca_scrollAreaWidgetContents.cursor().setPos(user.pos().x(),user.pos().y())
            # print(self.kp_chatArea.verticalScrollBar().value())
            self.kp_chatArea.verticalScrollBar().setValue((self.userDiasCnt+self.robertDiasCnt-4)*100)
        except Exception as e:
            print(e)

    def __add_line_end(self,text):
        linemax = 10
        for i in range(1,linemax):
            if i %10 == 0:
                text.insert(i,'\n')
        return text

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
