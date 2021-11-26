# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource_rc

class Ui_index(object):
    def setupUi(self, index):
        if not index.objectName():
            index.setObjectName(u"index")
        index.resize(1000, 618)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(index.sizePolicy().hasHeightForWidth())
        index.setSizePolicy(sizePolicy)
        index.setMinimumSize(QSize(1000, 618))
        index.setMaximumSize(QSize(1000, 618))
        index.setStyleSheet(u"background-color:rgb(224, 242, 255);\n"
"border: none;\n"
"font: 16px \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: #333333\n"
"")
        self.horizontalLayout = QHBoxLayout(index)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left = QFrame(index)
        self.left.setObjectName(u"left")
        self.left.setStyleSheet(u"\n"
"background-color:#2B579A;\n"
"text-align: left;")
        self.left.setFrameShape(QFrame.StyledPanel)
        self.left.setFrameShadow(QFrame.Raised)
        self.leftTop = QFrame(self.left)
        self.leftTop.setObjectName(u"leftTop")
        self.leftTop.setGeometry(QRect(0, 0, 240, 80))
        self.leftTop.setStyleSheet(u"background-color:#41A5EE;")
        self.leftTop.setFrameShape(QFrame.StyledPanel)
        self.leftTop.setFrameShadow(QFrame.Raised)
        self.headImg = QLabel(self.leftTop)
        self.headImg.setObjectName(u"headImg")
        self.headImg.setGeometry(QRect(16, 20, 40, 40))
        self.headImg.setMinimumSize(QSize(40, 40))
        self.headImg.setMaximumSize(QSize(40, 40))
        self.headImg.setStyleSheet(u"border-radius: 20px;\n"
"background-color: #fff;")
        self.uerName = QLabel(self.leftTop)
        self.uerName.setObjectName(u"uerName")
        self.uerName.setGeometry(QRect(68, 28, 71, 25))
        self.uerName.setMinimumSize(QSize(0, 25))
        self.uerName.setMaximumSize(QSize(16777215, 25))
        self.uerName.setStyleSheet(u"background-color:#41A5EE;")
        self.uerName.setTextFormat(Qt.PlainText)
        self.setButton = QToolButton(self.leftTop)
        self.setButton.setObjectName(u"setButton")
        self.setButton.setGeometry(QRect(208, 28, 24, 24))
        self.setButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.setButton.setStyleSheet(u"QToolButton {\n"
"background-color: none;\n"
"image: url(:/open/img/open/Setting_open_unselected.png)\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"	image: url(:/selected/img/selected/Setting_selected.png);\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"	image: url(:/selected/img/selected/Setting_selected.png);\n"
"}")
        self.kp = QFrame(self.left)
        self.kp.setObjectName(u"kp")
        self.kp.setGeometry(QRect(8, 104, 224, 40))
        self.kp.setCursor(QCursor(Qt.PointingHandCursor))
        self.kp.setStyleSheet(u"")
        self.kp.setFrameShape(QFrame.StyledPanel)
        self.kp.setFrameShadow(QFrame.Raised)
        self.kpButton = QPushButton(self.kp)
        self.kpButton.setObjectName(u"kpButton")
        self.kpButton.setGeometry(QRect(0, 0, 224, 40))
        self.kpButton.setMinimumSize(QSize(224, 40))
        self.kpButton.setMaximumSize(QSize(224, 40))
        self.kpButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.kpButton.setStyleSheet(u"QPushButton{\n"
"	background-color: #93D2FF;\n"
"	border-radius: 14px;\n"
"	padding:46px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: #FFFFFF;\n"
"}\n"
"")
        self.kpButton.setCheckable(True)
        self.kpIcon = QLabel(self.kp)
        self.kpIcon.setObjectName(u"kpIcon")
        self.kpIcon.setGeometry(QRect(16, 10, 24, 21))
        self.kpIcon.setStyleSheet(u"image: url(:/open/img/open/Chat_open_unselected.png);\n"
"background-color: none;")
        self.pm = QFrame(self.left)
        self.pm.setObjectName(u"pm")
        self.pm.setGeometry(QRect(8, 164, 224, 40))
        self.pm.setCursor(QCursor(Qt.PointingHandCursor))
        self.pm.setStyleSheet(u"")
        self.pm.setFrameShape(QFrame.StyledPanel)
        self.pm.setFrameShadow(QFrame.Raised)
        self.pmButton = QPushButton(self.pm)
        self.pmButton.setObjectName(u"pmButton")
        self.pmButton.setGeometry(QRect(0, 0, 224, 40))
        self.pmButton.setMinimumSize(QSize(224, 40))
        self.pmButton.setMaximumSize(QSize(224, 40))
        self.pmButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pmButton.setStyleSheet(u"QPushButton{\n"
"	background-color: #93D2FF;\n"
"	border-radius: 14px;\n"
"	padding:46px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #FFFFFF;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: #FFFFFF;\n"
"}\n"
"")
        self.pmButton.setCheckable(True)
        self.pmIcon = QLabel(self.pm)
        self.pmIcon.setObjectName(u"pmIcon")
        self.pmIcon.setGeometry(QRect(16, 10, 24, 21))
        self.pmIcon.setStyleSheet(u"image: url(:/open/img/open/Rank_open_unselected.png);\n"
"background-color: none;")
        self.sc = QFrame(self.left)
        self.sc.setObjectName(u"sc")
        self.sc.setGeometry(QRect(8, 284, 224, 40))
        self.sc.setCursor(QCursor(Qt.PointingHandCursor))
        self.sc.setFrameShape(QFrame.StyledPanel)
        self.sc.setFrameShadow(QFrame.Raised)
        self.scButton = QPushButton(self.sc)
        self.scButton.setObjectName(u"scButton")
        self.scButton.setGeometry(QRect(0, 0, 224, 40))
        self.scButton.setMinimumSize(QSize(224, 40))
        self.scButton.setMaximumSize(QSize(224, 40))
        self.scButton.setStyleSheet(u"QPushButton{\n"
"	background-color: #93D2FF;\n"
"	border-radius: 14px;\n"
"	padding:46px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #FFFFFF;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: #FFFFFF;\n"
"}\n"
"")
        self.scButton.setCheckable(True)
        self.scIcon = QLabel(self.sc)
        self.scIcon.setObjectName(u"scIcon")
        self.scIcon.setGeometry(QRect(16, 10, 24, 21))
        self.scIcon.setStyleSheet(u"image: url(:/open/img/open/Collect_open_unselected.png);\n"
"background-color: none;")
        self.qk = QFrame(self.left)
        self.qk.setObjectName(u"qk")
        self.qk.setGeometry(QRect(8, 224, 224, 40))
        self.qk.setCursor(QCursor(Qt.PointingHandCursor))
        self.qk.setFrameShape(QFrame.StyledPanel)
        self.qk.setFrameShadow(QFrame.Raised)
        self.tjButton = QPushButton(self.qk)
        self.tjButton.setObjectName(u"tjButton")
        self.tjButton.setGeometry(QRect(0, 0, 224, 40))
        self.tjButton.setMinimumSize(QSize(224, 40))
        self.tjButton.setMaximumSize(QSize(224, 40))
        self.tjButton.setStyleSheet(u"QPushButton{\n"
"	background-color: #93D2FF;\n"
"	border-radius: 14px;\n"
"	padding:46px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #FFFFFF;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: #FFFFFF;\n"
"}\n"
"")
        self.tjButton.setCheckable(True)
        self.thIcon = QLabel(self.qk)
        self.thIcon.setObjectName(u"thIcon")
        self.thIcon.setGeometry(QRect(16, 10, 24, 21))
        self.thIcon.setStyleSheet(u"image: url(:/open/img/open/Study_open_unselected.png);\n"
"background-color: none;")
        self.putAwayButton = QToolButton(self.left)
        self.putAwayButton.setObjectName(u"putAwayButton")
        self.putAwayButton.setGeometry(QRect(200, 580, 28, 28))
        self.putAwayButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.putAwayButton.setStyleSheet(u"image: url(:/chatting/img/Chatting/turnleft.png);")

        self.horizontalLayout.addWidget(self.left)

        self.right = QFrame(index)
        self.right.setObjectName(u"right")
        self.right.setFrameShape(QFrame.StyledPanel)
        self.right.setFrameShadow(QFrame.Raised)
        self.minimizeButton = QToolButton(self.right)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setGeometry(QRect(690, 10, 20, 20))
        icon = QIcon()
        icon.addFile(u":/frame/img/Frame/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon)
        self.closeButton = QToolButton(self.right)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(730, 10, 20, 20))
        icon1 = QIcon()
        icon1.addFile(u":/frame/img/Frame/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon1)
        self.right_pm = QFrame(self.right)
        self.right_pm.setObjectName(u"right_pm")
        self.right_pm.setGeometry(QRect(0, 0, 760, 618))
        self.right_pm.setFrameShape(QFrame.StyledPanel)
        self.right_pm.setFrameShadow(QFrame.Raised)
        self.winTitle_pm = QLabel(self.right_pm)
        self.winTitle_pm.setObjectName(u"winTitle_pm")
        self.winTitle_pm.setGeometry(QRect(0, 0, 760, 80))
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.winTitle_pm.setFont(font)
        self.winTitle_pm.setStyleSheet(u"font-size:32px;font-weight: 700;")
        self.winTitle_pm.setAlignment(Qt.AlignCenter)
        self.pm_myLearnTime = QFrame(self.right_pm)
        self.pm_myLearnTime.setObjectName(u"pm_myLearnTime")
        self.pm_myLearnTime.setGeometry(QRect(121, 112, 120, 120))
        self.pm_myLearnTime.setStyleSheet(u"background-color:#fff;\n"
"border-radius: 60px;")
        self.pm_myLearnTime.setFrameShape(QFrame.StyledPanel)
        self.pm_myLearnTime.setFrameShadow(QFrame.Raised)
        self.pm_mlt_title = QLabel(self.pm_myLearnTime)
        self.pm_mlt_title.setObjectName(u"pm_mlt_title")
        self.pm_mlt_title.setGeometry(QRect(0, 0, 120, 60))
        self.pm_mlt_title.setStyleSheet(u"background-color: none;\n"
"font-size: 20px;\n"
"color: #4A7CC6;\n"
"font-weight: 500;")
        self.pm_mlt_title.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.pm_mlt_detail = QLabel(self.pm_myLearnTime)
        self.pm_mlt_detail.setObjectName(u"pm_mlt_detail")
        self.pm_mlt_detail.setGeometry(QRect(0, 60, 120, 60))
        self.pm_mlt_detail.setStyleSheet(u"background-color: none;\n"
"font-size: 16px;\n"
"")
        self.pm_mlt_detail.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.pm_myRank = QFrame(self.right_pm)
        self.pm_myRank.setObjectName(u"pm_myRank")
        self.pm_myRank.setGeometry(QRect(321, 112, 120, 120))
        self.pm_myRank.setStyleSheet(u"background-color:#fff;\n"
"border-radius: 60px;")
        self.pm_myRank.setFrameShape(QFrame.StyledPanel)
        self.pm_myRank.setFrameShadow(QFrame.Raised)
        self.pm_mr_title = QLabel(self.pm_myRank)
        self.pm_mr_title.setObjectName(u"pm_mr_title")
        self.pm_mr_title.setGeometry(QRect(0, 0, 120, 60))
        self.pm_mr_title.setStyleSheet(u"background-color: none;\n"
"font-size: 20px;\n"
"color: #FF6D00;\n"
"font-weight: 500;")
        self.pm_mr_title.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.pm_mr_detail = QLabel(self.pm_myRank)
        self.pm_mr_detail.setObjectName(u"pm_mr_detail")
        self.pm_mr_detail.setGeometry(QRect(0, 60, 120, 60))
        self.pm_mr_detail.setStyleSheet(u"background-color: none;\n"
"font-size: 16px;\n"
"")
        self.pm_mr_detail.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.pm_myScore = QFrame(self.right_pm)
        self.pm_myScore.setObjectName(u"pm_myScore")
        self.pm_myScore.setGeometry(QRect(490, 110, 120, 120))
        self.pm_myScore.setStyleSheet(u"background-color:#fff;\n"
"border-radius: 60px;")
        self.pm_myScore.setFrameShape(QFrame.StyledPanel)
        self.pm_myScore.setFrameShadow(QFrame.Raised)
        self.pm_ms_title = QLabel(self.pm_myScore)
        self.pm_ms_title.setObjectName(u"pm_ms_title")
        self.pm_ms_title.setGeometry(QRect(0, 0, 120, 60))
        self.pm_ms_title.setStyleSheet(u"background-color: none;\n"
"font-size: 20px;\n"
"color: #4A7CC6;\n"
"font-weight: 500;")
        self.pm_ms_title.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.pm_ms_detail = QLabel(self.pm_myScore)
        self.pm_ms_detail.setObjectName(u"pm_ms_detail")
        self.pm_ms_detail.setGeometry(QRect(0, 60, 120, 60))
        self.pm_ms_detail.setStyleSheet(u"background-color: none;\n"
"font-size: 16px;\n"
"")
        self.pm_ms_detail.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.pm_rankList = QScrollArea(self.right_pm)
        self.pm_rankList.setObjectName(u"pm_rankList")
        self.pm_rankList.setGeometry(QRect(0, 275, 760, 340))
        self.pm_rankList.setWidgetResizable(True)
        self.pm_rl_scrollAreaWidgetContents = QWidget()
        self.pm_rl_scrollAreaWidgetContents.setObjectName(u"pm_rl_scrollAreaWidgetContents")
        self.pm_rl_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 760, 340))
        self.pm_rl_scrollAreaWidgetContents.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.pm_rl_scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 0, 15, 10)
        self.pm_rl_rankDetail = QFrame(self.pm_rl_scrollAreaWidgetContents)
        self.pm_rl_rankDetail.setObjectName(u"pm_rl_rankDetail")
        self.pm_rl_rankDetail.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 12px;\n"
"")
        self.pm_rl_rankDetail.setFrameShape(QFrame.StyledPanel)
        self.pm_rl_rankDetail.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.pm_rl_rankDetail)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(20, 10, 20, 10)
        self.pm_rl_rd_rank = QLabel(self.pm_rl_rankDetail)
        self.pm_rl_rd_rank.setObjectName(u"pm_rl_rd_rank")
        self.pm_rl_rd_rank.setStyleSheet(u"margin:0 0;")
        self.pm_rl_rd_rank.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.pm_rl_rd_rank)

        self.pm_rl_rd_Img = QPushButton(self.pm_rl_rankDetail)
        self.pm_rl_rd_Img.setObjectName(u"pm_rl_rd_Img")
        self.pm_rl_rd_Img.setMinimumSize(QSize(40, 40))
        self.pm_rl_rd_Img.setStyleSheet(u"margin:0 0;\n"
"background-color: #93D2FF;\n"
"border-radius: 20px")
        self.pm_rl_rd_Img.setIconSize(QSize(60, 60))

        self.horizontalLayout_4.addWidget(self.pm_rl_rd_Img)

        self.pm_rl_rd_name = QLabel(self.pm_rl_rankDetail)
        self.pm_rl_rd_name.setObjectName(u"pm_rl_rd_name")
        self.pm_rl_rd_name.setStyleSheet(u"margin:0 0;")

        self.horizontalLayout_4.addWidget(self.pm_rl_rd_name)

        self.pm_rl_rd_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.pm_rl_rd_horizontalSpacer)

        self.pm_rl_rd_learnTime = QLabel(self.pm_rl_rankDetail)
        self.pm_rl_rd_learnTime.setObjectName(u"pm_rl_rd_learnTime")
        self.pm_rl_rd_learnTime.setStyleSheet(u"margin:0 0;")
        self.pm_rl_rd_learnTime.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.pm_rl_rd_learnTime)

        self.pm_rl_rd_score = QLabel(self.pm_rl_rankDetail)
        self.pm_rl_rd_score.setObjectName(u"pm_rl_rd_score")
        self.pm_rl_rd_score.setStyleSheet(u"margin:0 0;")
        self.pm_rl_rd_score.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.pm_rl_rd_score)


        self.verticalLayout_2.addWidget(self.pm_rl_rankDetail)

        self.pm_rl_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.pm_rl_verticalSpacer)

        self.pm_rankList.setWidget(self.pm_rl_scrollAreaWidgetContents)
        self.right_tj = QFrame(self.right)
        self.right_tj.setObjectName(u"right_tj")
        self.right_tj.setGeometry(QRect(0, 0, 760, 618))
        self.right_tj.setFrameShape(QFrame.StyledPanel)
        self.right_tj.setFrameShadow(QFrame.Raised)
        self.winTitle_tj = QLabel(self.right_tj)
        self.winTitle_tj.setObjectName(u"winTitle_tj")
        self.winTitle_tj.setGeometry(QRect(0, 0, 760, 80))
        self.winTitle_tj.setFont(font)
        self.winTitle_tj.setStyleSheet(u"font-size:32px;\n"
"font-weight: 700;")
        self.winTitle_tj.setAlignment(Qt.AlignCenter)
        self.tj_times = QFrame(self.right_tj)
        self.tj_times.setObjectName(u"tj_times")
        self.tj_times.setGeometry(QRect(78, 116, 160, 160))
        self.tj_times.setStyleSheet(u"background-color:#fff;\n"
"border-radius: 20px;")
        self.tj_times.setFrameShape(QFrame.StyledPanel)
        self.tj_times.setFrameShadow(QFrame.Raised)
        self.tj_t_title = QLabel(self.tj_times)
        self.tj_t_title.setObjectName(u"tj_t_title")
        self.tj_t_title.setGeometry(QRect(0, 10, 160, 40))
        self.tj_t_title.setStyleSheet(u"font-size: 20px;\n"
"backgroun-color: none;\n"
"color: #2B579A;\n"
"font-weight: 500")
        self.tj_t_title.setAlignment(Qt.AlignCenter)
        self.tj_t_detail = QLabel(self.tj_times)
        self.tj_t_detail.setObjectName(u"tj_t_detail")
        self.tj_t_detail.setGeometry(QRect(0, 40, 160, 120))
        self.tj_t_detail.setStyleSheet(u"font-size: 72px;\n"
"backgroun-color: none;\n"
"font-weight: 500;")
        self.tj_t_detail.setAlignment(Qt.AlignCenter)
        self.tj_t_detail.raise_()
        self.tj_t_title.raise_()
        self.tj_learnTime = QFrame(self.right_tj)
        self.tj_learnTime.setObjectName(u"tj_learnTime")
        self.tj_learnTime.setGeometry(QRect(300, 116, 160, 160))
        self.tj_learnTime.setStyleSheet(u"background-color:#fff;\n"
"border-radius: 20px;")
        self.tj_learnTime.setFrameShape(QFrame.StyledPanel)
        self.tj_learnTime.setFrameShadow(QFrame.Raised)
        self.tj_lt_detail = QLabel(self.tj_learnTime)
        self.tj_lt_detail.setObjectName(u"tj_lt_detail")
        self.tj_lt_detail.setGeometry(QRect(0, 40, 160, 120))
        self.tj_lt_detail.setStyleSheet(u"font-size: 24px;\n"
"backgroun-color: none;\n"
"")
        self.tj_lt_detail.setAlignment(Qt.AlignCenter)
        self.tj_lt_title = QLabel(self.tj_learnTime)
        self.tj_lt_title.setObjectName(u"tj_lt_title")
        self.tj_lt_title.setGeometry(QRect(0, 10, 160, 40))
        self.tj_lt_title.setStyleSheet(u"font-size: 20px;\n"
"backgroun-color: none;\n"
"color: #2B579A;\n"
"font-weight: 500;")
        self.tj_lt_title.setAlignment(Qt.AlignCenter)
        self.tj_score = QFrame(self.right_tj)
        self.tj_score.setObjectName(u"tj_score")
        self.tj_score.setGeometry(QRect(522, 116, 160, 160))
        self.tj_score.setStyleSheet(u"background-color:#fff;\n"
"border-radius: 20px;")
        self.tj_score.setFrameShape(QFrame.StyledPanel)
        self.tj_score.setFrameShadow(QFrame.Raised)
        self.tj_s_detail = QLabel(self.tj_score)
        self.tj_s_detail.setObjectName(u"tj_s_detail")
        self.tj_s_detail.setGeometry(QRect(0, 40, 160, 120))
        self.tj_s_detail.setStyleSheet(u"font-size: 72px;\n"
"backgroun-color: none;\n"
"font-weight: 500;")
        self.tj_s_detail.setAlignment(Qt.AlignCenter)
        self.tj_s_title = QLabel(self.tj_score)
        self.tj_s_title.setObjectName(u"tj_s_title")
        self.tj_s_title.setGeometry(QRect(0, 10, 160, 40))
        self.tj_s_title.setStyleSheet(u"font-size: 20px;\n"
"backgroun-color: none;\n"
"color: #2B579A;\n"
"font-weight: 500;")
        self.tj_s_title.setAlignment(Qt.AlignCenter)
        self.tj_statistics = QScrollArea(self.right_tj)
        self.tj_statistics.setObjectName(u"tj_statistics")
        self.tj_statistics.setGeometry(QRect(0, 312, 760, 306))
        self.tj_statistics.setWidgetResizable(True)
        self.tj_s_scrollAreaWidgetContents = QWidget()
        self.tj_s_scrollAreaWidgetContents.setObjectName(u"tj_s_scrollAreaWidgetContents")
        self.tj_s_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 760, 306))
        self.tj_s_scrollAreaWidgetContents.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.tj_s_scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tj_s_Detail = QFrame(self.tj_s_scrollAreaWidgetContents)
        self.tj_s_Detail.setObjectName(u"tj_s_Detail")
        self.tj_s_Detail.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 12px;\n"
"")
        self.tj_s_Detail.setFrameShape(QFrame.StyledPanel)
        self.tj_s_Detail.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.tj_s_Detail)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(20, 10, 20, 10)
        self.tj_s_d_img = QPushButton(self.tj_s_Detail)
        self.tj_s_d_img.setObjectName(u"tj_s_d_img")
        self.tj_s_d_img.setMinimumSize(QSize(40, 40))
        self.tj_s_d_img.setStyleSheet(u"margin:0 0;\n"
"background-color: #93D2FF;\n"
"border-radius: 20px")
        self.tj_s_d_img.setIconSize(QSize(60, 60))

        self.horizontalLayout_5.addWidget(self.tj_s_d_img)

        self.tj_s_d_name = QLabel(self.tj_s_Detail)
        self.tj_s_d_name.setObjectName(u"tj_s_d_name")
        self.tj_s_d_name.setStyleSheet(u"margin:0 0;")

        self.horizontalLayout_5.addWidget(self.tj_s_d_name)

        self.tj_s_d_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.tj_s_d_horizontalSpacer)

        self.tj_s_d_learnTime = QLabel(self.tj_s_Detail)
        self.tj_s_d_learnTime.setObjectName(u"tj_s_d_learnTime")
        self.tj_s_d_learnTime.setStyleSheet(u"margin:0 0;")
        self.tj_s_d_learnTime.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.tj_s_d_learnTime)


        self.verticalLayout_4.addWidget(self.tj_s_Detail)

        self.tj_s_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.tj_s_verticalSpacer)

        self.tj_statistics.setWidget(self.tj_s_scrollAreaWidgetContents)
        self.right_sc = QFrame(self.right)
        self.right_sc.setObjectName(u"right_sc")
        self.right_sc.setGeometry(QRect(0, 0, 760, 618))
        self.right_sc.setFrameShape(QFrame.StyledPanel)
        self.right_sc.setFrameShadow(QFrame.Raised)
        self.winTitle_sc = QLabel(self.right_sc)
        self.winTitle_sc.setObjectName(u"winTitle_sc")
        self.winTitle_sc.setGeometry(QRect(0, 0, 760, 80))
        self.winTitle_sc.setFont(font)
        self.winTitle_sc.setStyleSheet(u"font-size:32px;\n"
"font-weight: 700;")
        self.winTitle_sc.setAlignment(Qt.AlignCenter)
        self.sc_search = QFrame(self.right_sc)
        self.sc_search.setObjectName(u"sc_search")
        self.sc_search.setGeometry(QRect(20, 96, 720, 48))
        self.sc_search.setStyleSheet(u"border-radius: 16px;\n"
"background-color: #ffffff;")
        self.sc_search.setFrameShape(QFrame.StyledPanel)
        self.sc_search.setFrameShadow(QFrame.Raised)
        self.hboxLayout = QHBoxLayout(self.sc_search)
        self.hboxLayout.setSpacing(15)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.hboxLayout.setContentsMargins(15, 0, 15, 0)
        self.sc_s_icon = QLabel(self.sc_search)
        self.sc_s_icon.setObjectName(u"sc_s_icon")
        self.sc_s_icon.setMinimumSize(QSize(25, 25))
        self.sc_s_icon.setStyleSheet(u"image: url(:/collect/img/Collect/search.png);")

        self.hboxLayout.addWidget(self.sc_s_icon)

        self.sc_s_input = QTextEdit(self.sc_search)
        self.sc_s_input.setObjectName(u"sc_s_input")
        self.sc_s_input.setMinimumSize(QSize(0, 48))
        self.sc_s_input.setMaximumSize(QSize(16777215, 48))
        self.sc_s_input.setStyleSheet(u"padding:10px 0;")
        self.sc_s_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sc_s_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.hboxLayout.addWidget(self.sc_s_input)

        self.sc_s_searchButton = QPushButton(self.sc_search)
        self.sc_s_searchButton.setObjectName(u"sc_s_searchButton")

        self.hboxLayout.addWidget(self.sc_s_searchButton)

        self.sc_collectDetail = QScrollArea(self.right_sc)
        self.sc_collectDetail.setObjectName(u"sc_collectDetail")
        self.sc_collectDetail.setGeometry(QRect(0, 160, 760, 455))
        self.sc_collectDetail.setMinimumSize(QSize(0, 0))
        self.sc_collectDetail.setMaximumSize(QSize(16777215, 16777215))
        self.sc_collectDetail.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.sc_collectDetail.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.sc_collectDetail.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.sc_collectDetail.setWidgetResizable(True)
        self.sc_cd_scrollAreaWidgetContents = QWidget()
        self.sc_cd_scrollAreaWidgetContents.setObjectName(u"sc_cd_scrollAreaWidgetContents")
        self.sc_cd_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 760, 455))
        self.verticalLayout_3 = QVBoxLayout(self.sc_cd_scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 0, 20, 10)
        self.sc_cd_detail = QFrame(self.sc_cd_scrollAreaWidgetContents)
        self.sc_cd_detail.setObjectName(u"sc_cd_detail")
        self.sc_cd_detail.setMinimumSize(QSize(720, 120))
        self.sc_cd_detail.setStyleSheet(u"background-color: #fff;\n"
"border-radius: 16px;\n"
"margin-buttom: 20px")
        self.sc_cd_detail.setFrameShape(QFrame.StyledPanel)
        self.sc_cd_detail.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.sc_cd_detail)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(20, 20, 20, 20)
        self.sc_cd_d_img = QLabel(self.sc_cd_detail)
        self.sc_cd_d_img.setObjectName(u"sc_cd_d_img")
        self.sc_cd_d_img.setMinimumSize(QSize(80, 80))
        self.sc_cd_d_img.setStyleSheet(u"background-color: #93D2FF;\n"
"border-radius:10px")

        self.horizontalLayout_6.addWidget(self.sc_cd_d_img)

        self.sc_cd_d_title = QLabel(self.sc_cd_detail)
        self.sc_cd_d_title.setObjectName(u"sc_cd_d_title")

        self.horizontalLayout_6.addWidget(self.sc_cd_d_title)

        self.sc_cd_d_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.sc_cd_d_horizontalSpacer)

        self.sc_cd_d_collectButton = QToolButton(self.sc_cd_detail)
        self.sc_cd_d_collectButton.setObjectName(u"sc_cd_d_collectButton")
        self.sc_cd_d_collectButton.setMinimumSize(QSize(28, 28))
        self.sc_cd_d_collectButton.setStyleSheet(u"QToolButton {\n"
"	image: url(:/collect/img/Collect/Collect_selected.png);\n"
"}\n"
"QToolButton:hover {\n"
"	image: url(:/collect/img/Collect/Collect_unselected.png);\n"
"}\n"
"QToolButton:checked {\n"
"	image: url(:/collect/img/Collect/Collect_unselected.png);\n"
"}")
        self.sc_cd_d_collectButton.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.sc_cd_d_collectButton)


        self.verticalLayout_3.addWidget(self.sc_cd_detail)

        self.sc_cd_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.sc_cd_verticalSpacer)

        self.sc_collectDetail.setWidget(self.sc_cd_scrollAreaWidgetContents)
        self.right_kp = QFrame(self.right)
        self.right_kp.setObjectName(u"right_kp")
        self.right_kp.setGeometry(QRect(0, 0, 760, 618))
        self.right_kp.setFrameShape(QFrame.StyledPanel)
        self.right_kp.setFrameShadow(QFrame.Raised)
        self.kp_inputFrame = QFrame(self.right_kp)
        self.kp_inputFrame.setObjectName(u"kp_inputFrame")
        self.kp_inputFrame.setGeometry(QRect(0, 450, 760, 168))
        self.kp_inputFrame.setStyleSheet(u"background-color:rgb(224, 242, 255);\n"
"\n"
"")
        self.kp_inputFrame.setFrameShape(QFrame.StyledPanel)
        self.kp_inputFrame.setFrameShadow(QFrame.Raised)
        self.kp_if_microphone = QToolButton(self.kp_inputFrame)
        self.kp_if_microphone.setObjectName(u"kp_if_microphone")
        self.kp_if_microphone.setGeometry(QRect(330, 34, 100, 100))
        self.kp_if_microphone.setCursor(QCursor(Qt.PointingHandCursor))
        self.kp_if_microphone.setStyleSheet(u"image: url(:/chatting/img/Chatting/microphone2.png);")
        self.kp_if_write = QFrame(self.kp_inputFrame)
        self.kp_if_write.setObjectName(u"kp_if_write")
        self.kp_if_write.setGeometry(QRect(0, 0, 760, 168))
        self.kp_if_write.setStyleSheet(u"background-color: #fff;")
        self.kp_if_write.setFrameShape(QFrame.StyledPanel)
        self.kp_if_write.setFrameShadow(QFrame.Raised)
        self.kp_if_w_sendEdit = QTextEdit(self.kp_if_write)
        self.kp_if_w_sendEdit.setObjectName(u"kp_if_w_sendEdit")
        self.kp_if_w_sendEdit.setGeometry(QRect(0, 42, 760, 126))
        self.kp_if_w_sendEdit.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.kp_if_w_sendEdit.setStyleSheet(u"padding-left: 10px;\n"
"padding-right: 10px;\n"
"")
        self.kp_if_w_emoji = QToolButton(self.kp_if_write)
        self.kp_if_w_emoji.setObjectName(u"kp_if_w_emoji")
        self.kp_if_w_emoji.setGeometry(QRect(15, 10, 25, 25))
        self.kp_if_w_emoji.setCursor(QCursor(Qt.PointingHandCursor))
        self.kp_if_w_emoji.setStyleSheet(u"image: url(:/chatting/img/Chatting/smile.png);")
        self.kp_if_w_send = QPushButton(self.kp_if_write)
        self.kp_if_w_send.setObjectName(u"kp_if_w_send")
        self.kp_if_w_send.setGeometry(QRect(686, 10, 64, 32))
        self.kp_if_w_send.setCursor(QCursor(Qt.PointingHandCursor))
        self.kp_if_w_send.setStyleSheet(u"QPushButton{\n"
"	background-color: #93D2FF;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #2B579A;\n"
"	color:#fff;\n"
"}\n"
"\n"
"")
        self.kp_if_w_speak = QToolButton(self.kp_if_write)
        self.kp_if_w_speak.setObjectName(u"kp_if_w_speak")
        self.kp_if_w_speak.setGeometry(QRect(50, 10, 25, 25))
        self.kp_if_w_speak.setCursor(QCursor(Qt.PointingHandCursor))
        self.kp_if_w_speak.setStyleSheet(u"image: url(:/chatting/img/Chatting/microphone.png);")
        self.kp_if_writeButton = QToolButton(self.kp_inputFrame)
        self.kp_if_writeButton.setObjectName(u"kp_if_writeButton")
        self.kp_if_writeButton.setGeometry(QRect(720, 130, 20, 20))
        self.kp_if_writeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.kp_if_writeButton.setStyleSheet(u"image: url(:/chatting/img/Chatting/type.png);")
        self.kp_if_writeButton.raise_()
        self.kp_if_microphone.raise_()
        self.kp_if_write.raise_()
        self.kp_changeButton = QToolButton(self.right_kp)
        self.kp_changeButton.setObjectName(u"kp_changeButton")
        self.kp_changeButton.setGeometry(QRect(720, 50, 20, 20))
        self.kp_changeButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/chatting/img/Chatting/exchange.png", QSize(), QIcon.Normal, QIcon.Off)
        self.kp_changeButton.setIcon(icon2)
        self.kp_chatArea = QScrollArea(self.right_kp)
        self.kp_chatArea.setObjectName(u"kp_chatArea")
        self.kp_chatArea.setGeometry(QRect(0, 80, 760, 370))
        self.kp_chatArea.setMaximumSize(QSize(760, 16777215))
        self.kp_chatArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.kp_chatArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.kp_chatArea.setWidgetResizable(True)
        self.kp_ca_scrollAreaWidgetContents = QWidget()
        self.kp_ca_scrollAreaWidgetContents.setObjectName(u"kp_ca_scrollAreaWidgetContents")
        self.kp_ca_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 762, 370))
        self.verticalLayout = QVBoxLayout(self.kp_ca_scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.kp_ca_robert = QFrame(self.kp_ca_scrollAreaWidgetContents)
        self.kp_ca_robert.setObjectName(u"kp_ca_robert")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.kp_ca_robert.sizePolicy().hasHeightForWidth())
        self.kp_ca_robert.setSizePolicy(sizePolicy1)
        self.kp_ca_robert.setMaximumSize(QSize(740, 16777215))
        self.kp_ca_robert.setFrameShape(QFrame.StyledPanel)
        self.kp_ca_robert.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.kp_ca_robert)
        self.horizontalLayout_2.setSpacing(16)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(25, 5, 300, 5)
        self.kp_ca_r_img = QLabel(self.kp_ca_robert)
        self.kp_ca_r_img.setObjectName(u"kp_ca_r_img")
        self.kp_ca_r_img.setMinimumSize(QSize(48, 48))
        self.kp_ca_r_img.setMaximumSize(QSize(48, 48))
        self.kp_ca_r_img.setStyleSheet(u"border-radius: 24px;\n"
"background-color: #fff;")

        self.horizontalLayout_2.addWidget(self.kp_ca_r_img)

        self.kp_ca_r_text = QLabel(self.kp_ca_robert)
        self.kp_ca_r_text.setObjectName(u"kp_ca_r_text")
        self.kp_ca_r_text.setEnabled(True)
        sizePolicy.setHeightForWidth(self.kp_ca_r_text.sizePolicy().hasHeightForWidth())
        self.kp_ca_r_text.setSizePolicy(sizePolicy)
        self.kp_ca_r_text.setMaximumSize(QSize(16777215, 16777215))
        self.kp_ca_r_text.setStyleSheet(u"background-color: #ffffff;\n"
"border-radius: 12px;\n"
"padding:4px")
        self.kp_ca_r_text.setFrameShape(QFrame.Box)
        self.kp_ca_r_text.setFrameShadow(QFrame.Plain)
        self.kp_ca_r_text.setTextFormat(Qt.RichText)

        self.horizontalLayout_2.addWidget(self.kp_ca_r_text)

        self.kp_ca_r_horizontalSpacer = QSpacerItem(700, 48, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.kp_ca_r_horizontalSpacer)

        self.horizontalLayout_2.setStretch(0, 80)

        self.verticalLayout.addWidget(self.kp_ca_robert)

        self.kp_ca_myUser = QFrame(self.kp_ca_scrollAreaWidgetContents)
        self.kp_ca_myUser.setObjectName(u"kp_ca_myUser")
        sizePolicy1.setHeightForWidth(self.kp_ca_myUser.sizePolicy().hasHeightForWidth())
        self.kp_ca_myUser.setSizePolicy(sizePolicy1)
        self.kp_ca_myUser.setMaximumSize(QSize(740, 16777215))
        self.kp_ca_myUser.setLayoutDirection(Qt.RightToLeft)
        self.kp_ca_myUser.setFrameShape(QFrame.StyledPanel)
        self.kp_ca_myUser.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.kp_ca_myUser)
        self.horizontalLayout_3.setSpacing(16)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(300, 5, 25, 5)
        self.kp_ca_mu_img = QLabel(self.kp_ca_myUser)
        self.kp_ca_mu_img.setObjectName(u"kp_ca_mu_img")
        self.kp_ca_mu_img.setMinimumSize(QSize(48, 48))
        self.kp_ca_mu_img.setMaximumSize(QSize(48, 48))
        self.kp_ca_mu_img.setStyleSheet(u"border-radius: 24px;\n"
"background-color: #fff;")

        self.horizontalLayout_3.addWidget(self.kp_ca_mu_img)

        self.kp_ca_mu_text = QLabel(self.kp_ca_myUser)
        self.kp_ca_mu_text.setObjectName(u"kp_ca_mu_text")
        self.kp_ca_mu_text.setEnabled(True)
        sizePolicy.setHeightForWidth(self.kp_ca_mu_text.sizePolicy().hasHeightForWidth())
        self.kp_ca_mu_text.setSizePolicy(sizePolicy)
        self.kp_ca_mu_text.setMaximumSize(QSize(16777215, 16777215))
        self.kp_ca_mu_text.setLayoutDirection(Qt.RightToLeft)
        self.kp_ca_mu_text.setStyleSheet(u"background-color: #93D2FF;\n"
"	border-radius: 12px;\n"
"	padding:4px")
        self.kp_ca_mu_text.setInputMethodHints(Qt.ImhNone)
        self.kp_ca_mu_text.setFrameShape(QFrame.NoFrame)
        self.kp_ca_mu_text.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_3.addWidget(self.kp_ca_mu_text)

        self.kp_ca_mu_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.kp_ca_mu_horizontalSpacer)

        self.horizontalLayout_3.setStretch(0, 80)

        self.verticalLayout.addWidget(self.kp_ca_myUser)

        self.kp_ca_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.kp_ca_verticalSpacer)

        self.kp_chatArea.setWidget(self.kp_ca_scrollAreaWidgetContents)
        self.winTitle_kp = QLabel(self.right_kp)
        self.winTitle_kp.setObjectName(u"winTitle_kp")
        self.winTitle_kp.setGeometry(QRect(0, 0, 760, 80))
        self.winTitle_kp.setFont(font)
        self.winTitle_kp.setStyleSheet(u"font-size:32px;\n"
"font-weight: 700;")
        self.winTitle_kp.setAlignment(Qt.AlignCenter)
        self.kp_inputFrame.raise_()
        self.kp_chatArea.raise_()
        self.winTitle_kp.raise_()
        self.kp_changeButton.raise_()
        self.right_pm.raise_()
        self.right_sc.raise_()
        self.right_tj.raise_()
        self.right_kp.raise_()
        self.closeButton.raise_()
        self.minimizeButton.raise_()

        self.horizontalLayout.addWidget(self.right)

        self.horizontalLayout.setStretch(0, 24)
        self.horizontalLayout.setStretch(1, 76)

        self.retranslateUi(index)
        self.closeButton.clicked.connect(index.close)
        self.minimizeButton.clicked.connect(index.showMinimized)
        self.pmButton.clicked.connect(self.right_pm.show)
        self.pmButton.clicked.connect(self.right_kp.close)
        self.pmButton.clicked.connect(self.right_sc.close)
        self.pmButton.clicked.connect(self.right_tj.close)
        self.tjButton.clicked.connect(self.right_tj.show)
        self.scButton.clicked.connect(self.right_tj.close)
        self.kpButton.clicked.connect(self.right_tj.close)
        self.scButton.clicked.connect(self.right_sc.show)
        self.tjButton.clicked.connect(self.right_sc.close)
        self.kpButton.clicked.connect(self.right_sc.close)
        self.kpButton.clicked.connect(self.right_pm.close)
        self.tjButton.clicked.connect(self.right_pm.close)
        self.kpButton.clicked.connect(self.right_kp.show)
        self.scButton.clicked.connect(self.right_kp.close)
        self.scButton.clicked.connect(self.right_pm.close)
        self.tjButton.clicked.connect(self.right_kp.close)
        self.kp_if_w_speak.clicked.connect(self.kp_if_microphone.show)
        self.kp_if_writeButton.clicked.connect(self.kp_if_write.show)
        self.kp_if_writeButton.clicked.connect(self.kp_if_microphone.close)
        self.kp_if_w_speak.clicked.connect(self.kp_if_write.close)
        self.kp_if_writeButton.clicked.connect(self.kp_if_writeButton.close)
        self.kp_if_w_speak.clicked.connect(self.kp_if_writeButton.show)

        QMetaObject.connectSlotsByName(index)
    # setupUi

    def retranslateUi(self, index):
        index.setWindowTitle(QCoreApplication.translate("index", u"Form", None))
        self.headImg.setText("")
        self.uerName.setText(QCoreApplication.translate("index", u"\u7528\u6237\u540d", None))
        self.setButton.setText("")
        self.kpButton.setText(QCoreApplication.translate("index", u"\u79d1\u666e\u804a\u5929", None))
        self.kpIcon.setText("")
        self.pmButton.setText(QCoreApplication.translate("index", u"\u6392\u540d", None))
        self.pmIcon.setText("")
        self.scButton.setText(QCoreApplication.translate("index", u"\u6536\u85cf", None))
        self.scIcon.setText("")
        self.tjButton.setText(QCoreApplication.translate("index", u"\u7edf\u8ba1", None))
        self.thIcon.setText("")
        self.putAwayButton.setText("")
        self.minimizeButton.setText(QCoreApplication.translate("index", u"...", None))
        self.closeButton.setText("")
        self.winTitle_pm.setText(QCoreApplication.translate("index", u"\u6392   \u540d", None))
        self.pm_mlt_title.setText(QCoreApplication.translate("index", u"\u5b66\u4e60\u65f6\u957f", None))
        self.pm_mlt_detail.setText(QCoreApplication.translate("index", u"24\u5c0f\u65f656\u5206", None))
        self.pm_mr_title.setText(QCoreApplication.translate("index", u"\u5f53\u524d\u6392\u540d", None))
        self.pm_mr_detail.setText(QCoreApplication.translate("index", u"2", None))
        self.pm_ms_title.setText(QCoreApplication.translate("index", u"\u6211\u7684\u79ef\u5206", None))
        self.pm_ms_detail.setText(QCoreApplication.translate("index", u"300", None))
        self.pm_rl_rd_rank.setText(QCoreApplication.translate("index", u"1", None))
        self.pm_rl_rd_Img.setText("")
        self.pm_rl_rd_name.setText(QCoreApplication.translate("index", u"apple", None))
        self.pm_rl_rd_learnTime.setText(QCoreApplication.translate("index", u"24\u5c0f\u65f656\u5206", None))
        self.pm_rl_rd_score.setText(QCoreApplication.translate("index", u"300\u5206", None))
        self.winTitle_tj.setText(QCoreApplication.translate("index", u"\u7edf   \u8ba1", None))
        self.tj_t_title.setText(QCoreApplication.translate("index", u"\u4eca\u65e5\u5b66\u4e60\u6b21\u6570", None))
        self.tj_t_detail.setText(QCoreApplication.translate("index", u"33", None))
        self.tj_lt_detail.setText(QCoreApplication.translate("index", u"1\u5c0f\u65f68\u5206", None))
        self.tj_lt_title.setText(QCoreApplication.translate("index", u"\u4eca\u65e5\u5b66\u4e60\u65f6\u957f", None))
        self.tj_s_detail.setText(QCoreApplication.translate("index", u"68", None))
        self.tj_s_title.setText(QCoreApplication.translate("index", u"\u4eca\u65e5\u83b7\u5f97\u79ef\u5206", None))
        self.tj_s_d_img.setText("")
        self.tj_s_d_name.setText(QCoreApplication.translate("index", u"\u82f9\u679c\u7684\u4e00\u767e\u79cd\u5403\u6cd5", None))
        self.tj_s_d_learnTime.setText(QCoreApplication.translate("index", u"0\u5c0f\u65f656\u5206", None))
        self.winTitle_sc.setText(QCoreApplication.translate("index", u"\u6536   \u85cf", None))
        self.sc_s_icon.setText("")
        self.sc_s_input.setHtml(QCoreApplication.translate("index", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; font-size:16px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">    </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:48px; background-color:#7fffd4;\"><br /></p></body></html>", None))
        self.sc_s_searchButton.setText(QCoreApplication.translate("index", u"\u641c\u7d22", None))
        self.sc_cd_d_img.setText("")
        self.sc_cd_d_title.setText(QCoreApplication.translate("index", u"\u82f9\u679c\u7684\u4e00\u767e\u79cd\u5403\u6cd5", None))
        self.sc_cd_d_collectButton.setText("")
        self.kp_if_microphone.setText("")
        self.kp_if_w_emoji.setText("")
        self.kp_if_w_send.setText(QCoreApplication.translate("index", u"\u53d1\u9001", None))
        self.kp_if_w_speak.setText("")
        self.kp_if_writeButton.setText("")
        self.kp_changeButton.setText("")
        self.kp_ca_r_img.setText("")
        self.kp_ca_r_text.setText(QCoreApplication.translate("index", u"\u4f60\u597d\uff0c\u6211\u662f\u804a\u5929\u673a\u5668\u4eba\uff0c\u5c0f\u4eba\u7684\u996d\u5361\u98de\u673a\u5f00", None))
        self.kp_ca_mu_img.setText("")
        self.kp_ca_mu_text.setText(QCoreApplication.translate("index", u"\u54c8\u54c8\u54c8\u54c8\u54c8\u54c8\u54c8\u54c8\u54c8\u54c8\u54c8\u54c8\u54c8\u54c8\u54c8", None))
        self.winTitle_kp.setText(QCoreApplication.translate("index", u"\u79d1   \u79d1", None))
    # retranslateUi

