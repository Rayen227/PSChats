import pyaudio
import wave
import os
from time import sleep
# import threading
from PyQt5.Qt import QThread
import numpy as np

SUCCESS = 0
FAIL = 1

class AudioRecorder(QThread):

    def __init__(self):
        super().__init__()
        self.CHUNK = 1024  # 每个缓冲区的帧数
        self.FORMAT = pyaudio.paInt16  # 采样位数
        self.CHANNELS = 1  # 单声道
        self.RATE = 44100  # 采样频率
        self.recordOn = True  # 是否录音
        self.delay = 0.05
        self.wave_out_path = 'cache/cache01.wav'
        self.callback = lambda :print('callback missing ...')
        self.p = pyaudio.PyAudio()  # 实例化对象
        self.stream = self.p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)  # 打开流，传入响应参数
        self.wf = wave.open(self.wave_out_path, 'wb')  # 打开 wav 文件。
        self.wf.setnchannels(self.CHANNELS)  # 声道设置
        self.wf.setsampwidth(self.p.get_sample_size(self.FORMAT))  # 采样位数设置
        self.wf.setframerate(self.RATE)  # 采样频率设置

    def setCallback(self,callback):
        self.callback=callback

    def stopRecord(self):
        self.recordOn = False

    def isRecordOn(self):
        return self.recordOn

    def run(self):
        record_second = 0.5
        while (self.recordOn):
            for _ in range(0, int(self.RATE * record_second / self.CHUNK)):
                self.data = self.stream.read(self.CHUNK)
                self.wf.writeframes(self.data)  # 写入数据
            # sleep(self.delay)
        self.stream.stop_stream()  # 关闭流
        self.stream.close()
        self.p.terminate()
        self.wf.close()
        self.recordOn=False
        print("录音结束")
        self.callback()


class AudioPlayer(QThread):

    def __init__(self):
        super().__init__()
        self.CHUNK = 1024  # 每个缓冲区的帧数
        self.FORMAT = pyaudio.paInt16  # 采样位数
        self.CHANNELS = 1  # 单声道
        self.RATE = 44100  # 采样频率
        self.wave_input_path = 'cache/test.wav'
        self.p = pyaudio.PyAudio()  # 实例化
        self.wf = wave.open(self.wave_input_path, 'rb')  # 读 wav 文件
        self.stream = self.p.open(
                        format=self.p.get_format_from_width(self.wf.getsampwidth()),
                        channels=self.wf.getnchannels(),
                        rate=self.wf.getframerate(),
                        output=True)

    def run(self):
        data = self.wf.readframes(self.CHUNK)  # 读数据
        while len(data) > 0:
            self.stream.write(data)
            data = self.wf.readframes(self.CHUNK)

        self.stream.stop_stream()  # 关闭资源
        self.stream.close()
        self.p.terminate()
        print("播放结束")


