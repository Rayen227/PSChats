from PyQt5.Qt import QThread
from concurrent.futures import ThreadPoolExecutor
from time import sleep
class NN():
    def __init__(self):
        super().__init__()
        self.output = ''
        self.sinal = 0

    def test(self,text):
        sleep(2)
        return text + '的回答。'



# class NN(QThread):
#     def __init__(self,text_input):
#         super().__init__()
#         self.input = text_input
#         self.output = ''
#         self.sinal = 0
#
#
#     def run(self):
#         try:
#             sleep(2)
#             print('runing')
#             self.output = self.input+'的回答。'
#             self.sinal = 1
#
#         except Exception as e:
#             print(e)
#         else:
#             print('yes')
#
