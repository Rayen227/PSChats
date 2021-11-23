import pyaudio
import wave
import os
from time import sleep
import threading
import numpy as np

SUCCESS = 0
FAIL = 1

class AutoAudioManager(threading.Thread):

    def __init__(self):
        super().__init__()
        self.CHUNK = 1024  # 每个缓冲区的帧数
        self.FORMAT = pyaudio.paInt16  # 采样位数
        self.CHANNELS = 1  # 单声道
        self.RATE = 44100  # 采样频率
        self.recordOn = True  # 是否录音
        self.delay = 0.05
        self.wave_out_path = 'cache/cache01.wav'
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

    def stopRecord(self):
        self.recordOn = False

    def run(self):
        record_second = 1
        while (self.recordOn):
            for _ in range(0, int(self.RATE * record_second / self.CHUNK)):
                self.data = self.stream.read(self.CHUNK)
                self.wf.writeframes(self.data)  # 写入数据
            sleep(self.delay)
        self.stream.stop_stream()  # 关闭流
        self.stream.close()
        self.p.terminate()
        self.wf.close()
        print("录音结束")


'''
用于实现语音模块的输入和输出
'''
class AudioManager:
    CHUNK = 1024  # 每个缓冲区的帧数
    FORMAT = pyaudio.paInt16  # 采样位数
    CHANNELS = 1  # 单声道
    RATE = 44100  # 采样频率

    def record_audio(self, wave_out_path, record_second):
        """ 录音功能 """
        p = pyaudio.PyAudio()  # 实例化对象
        stream = p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)  # 打开流，传入响应参数
        wf = wave.open(wave_out_path, 'wb')  # 打开 wav 文件。
        wf.setnchannels(self.CHANNELS)  # 声道设置
        wf.setsampwidth(p.get_sample_size(self.FORMAT))  # 采样位数设置
        wf.setframerate(self.RATE)  # 采样频率设置

        for _ in range(0, int(self.RATE * record_second / self.CHUNK)):
            data = stream.read(self.CHUNK)
            wf.writeframes(data)  # 写入数据
            print(data)
        stream.stop_stream()  # 关闭流
        stream.close()
        p.terminate()
        wf.close()


    def playAudio(self, wave_input_path):
        p = pyaudio.PyAudio()  # 实例化
        wf = wave.open(wave_input_path, 'rb')  # 读 wav 文件
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        data = wf.readframes(self.CHUNK)  # 读数据
        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(self.CHUNK)

        stream.stop_stream()  # 关闭资源
        stream.close()
        p.terminate()

