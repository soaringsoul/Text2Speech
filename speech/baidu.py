from aip import AipSpeech
from PyQt5 import QtCore
import os
import time


class Speech(QtCore.QThread):
    progress_signal = QtCore.pyqtSignal(str)

    def __init__(self,
                 APP_ID="18502870",
                 API_KEY="4m8Bh3Ncbv5LM9rl13ubRFjI",
                 SECRET_KEY="bd1DqAQhxOvGoEDWLASsWthDpa78GhGA",
                 per=0,
                 vol=5,
                 spd=5,
                 pit=5,
                 text="你好，这是夜雨微寒开发的，语音合成小助手！欢迎使用哦！"

                 ):
        '''
        你的百度 APPID AK SK
        :param APP_ID:
        :param API_KEY:
        :param SECRET_KEY:
        '''
        super(Speech, self).__init__()
        self.APP_ID = APP_ID
        self.API_KEY = API_KEY
        self.SECRET_KEY = SECRET_KEY
        self.per = per
        self.vol = vol
        self.spd = spd
        self.pit = pit
        self.text = text

    def run(self):

        client = AipSpeech(self.APP_ID, self.API_KEY, self.SECRET_KEY)
        result = client.synthesis('%s' % self.text, 'zh', 1, {
            'vol': self.vol, 'pit': self.pit, 'per': self.per, 'spd': self.spd,
        })
        self.progress_signal.emit("合成语音成功，开始写入音频文件到本地!")
        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            speech_path = os.path.join(os.getcwd(), "audio")
            if not os.path.exists(speech_path):
                os.makedirs(speech_path)
            audio_name = time.strftime("%Y-%m-%d_%H-%M-%S") + self.text[:10]
            with open('%s/%s.mp3' % (speech_path, audio_name), 'wb') as f:
                f.write(result)
            self.progress_signal.emit("语音文件已被成功写入本地")
        else:
            self.progress_signal.emit("文本转语音失败，请确认输入的文本字节长度是否小于512个!")


if __name__ == "__main__":
    speech = Speech()
    speech.start()
