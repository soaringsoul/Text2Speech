# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\github_projects\txt2voice\ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(501, 519)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_voice = QtWidgets.QLabel(self.centralwidget)
        self.label_voice.setObjectName("label_voice")
        self.gridLayout.addWidget(self.label_voice, 0, 0, 1, 1)
        self.comboBox_voice = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_voice.setObjectName("comboBox_voice")
        self.comboBox_voice.addItem("")
        self.comboBox_voice.addItem("")
        self.comboBox_voice.addItem("")
        self.comboBox_voice.addItem("")
        self.gridLayout.addWidget(self.comboBox_voice, 0, 1, 1, 1)
        self.label_ = QtWidgets.QLabel(self.centralwidget)
        self.label_.setObjectName("label_")
        self.gridLayout.addWidget(self.label_, 2, 0, 1, 1)
        self.spinBox_speed = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_speed.setMaximum(9)
        self.spinBox_speed.setSingleStep(1)
        self.spinBox_speed.setDisplayIntegerBase(10)
        self.spinBox_speed.setObjectName("spinBox_speed")
        self.gridLayout.addWidget(self.spinBox_speed, 1, 1, 1, 1)
        self.spinBox_pit = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_pit.setMaximum(9)
        self.spinBox_pit.setObjectName("spinBox_pit")
        self.gridLayout.addWidget(self.spinBox_pit, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_speed = QtWidgets.QLabel(self.centralwidget)
        self.label_speed.setObjectName("label_speed")
        self.gridLayout.addWidget(self.label_speed, 1, 0, 1, 1)
        self.spinBox_vol = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_vol.setMaximum(15)
        self.spinBox_vol.setObjectName("spinBox_vol")
        self.gridLayout.addWidget(self.spinBox_vol, 3, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.label_progress = QtWidgets.QLabel(self.centralwidget)
        self.label_progress.setText("")
        self.label_progress.setObjectName("label_progress")
        self.gridLayout_2.addWidget(self.label_progress, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "百度语音合成小助手"))
        self.textEdit.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">欢迎使用百度语音合成小助手，请输入文字！</p></body></html>"))
        self.label_voice.setText(_translate("mainWindow", "声音选择"))
        self.comboBox_voice.setItemText(0, _translate("mainWindow", "普通女声"))
        self.comboBox_voice.setItemText(1, _translate("mainWindow", "普通男声"))
        self.comboBox_voice.setItemText(2, _translate("mainWindow", "男声-度逍遥"))
        self.comboBox_voice.setItemText(3, _translate("mainWindow", "童声-度丫丫"))
        self.label_.setText(_translate("mainWindow", "音调"))
        self.label_4.setText(_translate("mainWindow", "音量"))
        self.label_speed.setText(_translate("mainWindow", "语速"))
        self.pushButton_2.setText(_translate("mainWindow", "打开语音文件夹"))
        self.pushButton.setText(_translate("mainWindow", "合成语音"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
