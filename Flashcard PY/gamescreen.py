# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QtCore.QSize(900, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/flash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"background-image: url(:/icons/voca2.png);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMinimumSize(QtCore.QSize(50, 50))
        self.label_6.setMaximumSize(QtCore.QSize(50, 50))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/icons/idea.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(135, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(50, 50))
        self.label.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/idea.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.game_icd_timer = QtWidgets.QLCDNumber(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game_icd_timer.sizePolicy().hasHeightForWidth())
        self.game_icd_timer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.game_icd_timer.setFont(font)
        self.game_icd_timer.setStyleSheet("color: rgb(0, 255, 127);\n"
"color: rgb(0, 0, 255);")
        self.game_icd_timer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.game_icd_timer.setFrameShadow(QtWidgets.QFrame.Plain)
        self.game_icd_timer.setLineWidth(2)
        self.game_icd_timer.setMidLineWidth(0)
        self.game_icd_timer.setSmallDecimalPoint(False)
        self.game_icd_timer.setMode(QtWidgets.QLCDNumber.Dec)
        self.game_icd_timer.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.game_icd_timer.setProperty("value", 3.0)
        self.game_icd_timer.setObjectName("game_icd_timer")
        self.horizontalLayout.addWidget(self.game_icd_timer)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 5)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalFrame = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame.setStyleSheet("#verticalFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(168, 255, 120, 255), stop:1 rgba(120, 255, 214, 255));\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.423, y2:0.570652, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(170, 255, 255, 255));\n"
"\n"
"border-radius: 25px;\n"
"}")
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.game_txt_language = QtWidgets.QLabel(self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game_txt_language.sizePolicy().hasHeightForWidth())
        self.game_txt_language.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.game_txt_language.setFont(font)
        self.game_txt_language.setAlignment(QtCore.Qt.AlignCenter)
        self.game_txt_language.setObjectName("game_txt_language")
        self.verticalLayout.addWidget(self.game_txt_language)
        self.game_txt_word = QtWidgets.QLabel(self.verticalFrame)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.game_txt_word.setFont(font)
        self.game_txt_word.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.game_txt_word.setAlignment(QtCore.Qt.AlignCenter)
        self.game_txt_word.setObjectName("game_txt_word")
        self.verticalLayout.addWidget(self.game_txt_word)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout_2.addWidget(self.verticalFrame)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.game_progres_bar = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game_progres_bar.sizePolicy().hasHeightForWidth())
        self.game_progres_bar.setSizePolicy(sizePolicy)
        self.game_progres_bar.setMinimum(0)
        self.game_progres_bar.setMaximum(20)
        self.game_progres_bar.setProperty("value", 12)
        self.game_progres_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.game_progres_bar.setOrientation(QtCore.Qt.Horizontal)
        self.game_progres_bar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.game_progres_bar.setObjectName("game_progres_bar")
        self.horizontalLayout_4.addWidget(self.game_progres_bar)
        self.game_txt_skor = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.game_txt_skor.setFont(font)
        self.game_txt_skor.setTextFormat(QtCore.Qt.AutoText)
        self.game_txt_skor.setObjectName("game_txt_skor")
        self.horizontalLayout_4.addWidget(self.game_txt_skor)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.game_btn_no = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game_btn_no.sizePolicy().hasHeightForWidth())
        self.game_btn_no.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.game_btn_no.setFont(font)
        self.game_btn_no.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.game_btn_no.setStyleSheet("border: none")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/cross1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.game_btn_no.setIcon(icon1)
        self.game_btn_no.setIconSize(QtCore.QSize(50, 50))
        self.game_btn_no.setObjectName("game_btn_no")
        self.horizontalLayout_6.addWidget(self.game_btn_no)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.game_btn_yes = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game_btn_yes.sizePolicy().hasHeightForWidth())
        self.game_btn_yes.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.game_btn_yes.setFont(font)
        self.game_btn_yes.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.game_btn_yes.setStyleSheet("border:none\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/check2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.game_btn_yes.setIcon(icon2)
        self.game_btn_yes.setIconSize(QtCore.QSize(50, 50))
        self.game_btn_yes.setObjectName("game_btn_yes")
        self.horizontalLayout_6.addWidget(self.game_btn_yes)
        self.horizontalLayout_6.setStretch(0, 4)
        self.horizontalLayout_6.setStretch(1, 4)
        self.horizontalLayout_6.setStretch(2, 4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.setStretch(0, 4)
        self.verticalLayout_2.setStretch(3, 1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem9)
        self.game_btn_back = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game_btn_back.sizePolicy().hasHeightForWidth())
        self.game_btn_back.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.game_btn_back.setFont(font)
        self.game_btn_back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.game_btn_back.setStyleSheet("border: none\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.game_btn_back.setIcon(icon3)
        self.game_btn_back.setIconSize(QtCore.QSize(100, 30))
        self.game_btn_back.setObjectName("game_btn_back")
        self.verticalLayout_6.addWidget(self.game_btn_back)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem10)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 2)
        self.verticalLayout_4.setStretch(2, 11)
        self.verticalLayout_4.setStretch(3, 2)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FLASHCARD"))
        self.label_5.setText(_translate("MainWindow", "ketadev"))
        self.label_4.setText(_translate("MainWindow", "FLASH CARDS"))
        self.label_2.setText(_translate("MainWindow", "ketadev"))
        self.game_txt_language.setText(_translate("MainWindow", "Dutch"))
        self.game_txt_word.setText(_translate("MainWindow", "Goedemorgen"))
        self.game_progres_bar.setFormat(_translate("MainWindow", "%p%"))
        self.game_txt_skor.setText(_translate("MainWindow", "12/20"))
        self.game_btn_no.setText(_translate("MainWindow", "False"))
        self.game_btn_yes.setText(_translate("MainWindow", "True"))
        self.game_btn_back.setText(_translate("MainWindow", "Main Menu"))
import dsa_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
