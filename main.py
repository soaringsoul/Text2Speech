# 导入python 自带库

# 导入自定义模块
from speech.baidu import Speech
from Mainwindow.Mainwindow import Ui_mainWindow
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QFileDialog

import os


class BaiduSpeech(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self):
        super(BaiduSpeech, self).__init__()
        self.setupUi(self)
        icon2 = QtGui.QIcon(':/icon2/soaringsoul.jpg')
        self.setWindowIcon(icon2)
        qss = open('./Mainwindow/Mainwindow.qss').read()
        self.setStyleSheet(qss)
        self.init_app()

    def setBrowerPath(self):
        pass

    def init_app(self):
        voice_dict = {
            '普通女声': 0,
            "普通男声": 1,
            "男声-度逍遥": 3,
            "童声-度丫丫": 4
        }

        # 0为女声，1为男声， 3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女
        self.voice = voice_dict.get(self.comboBox_voice.currentText(), 0)
        # int类型
        self.vol = self.spinBox_vol.value()
        self.speed = self.spinBox_speed.value()
        self.pit = self.spinBox_pit.value()
        self.text = self.textEdit.toPlainText()

    # 定义按下 开始抓取 按钮后的操作
    @pyqtSlot()
    def on_pushButton_to_speech_clicked(self):
        self.init_app()
        self.progress_signal_display("开始进行语音合成！")
        self.to_speech()

    @pyqtSlot()
    def on_pushButton_open_folder_clicked(self):
        self.open_speech_folder()

    def to_speech(self):
        try:
            self.speech = Speech(text=self.text,vol=self.vol,pit=self.pit,spd=self.speed, per=self.voice)
            self.speech.progress_signal.connect(self.progress_signal_display)
            self.speech.start()
        except Exception as e:
            print(e)

    def progress_signal_display(self, log_info):
        self.label_progress.setText(log_info)

    def error_message(self, error_info):
        self.label_progress.setText(error_info)

    def open_speech_folder(self):
        speech_path = os.path.join(os.getcwd(), "audio")
        # print(speech_path)
        if not os.path.exists(speech_path):
            os.makedirs(speech_path)

        os.system('explorer.exe /n, %s' % speech_path)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    bd_speech = BaiduSpeech()
    bd_speech.show()
    sys.exit(app.exec_())
