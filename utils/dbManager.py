import requests

host = 'http://47.107.112.158:5000'

'''
封装程序的基本数据库操作
'''
class DBManager:
    def __init__(self):
        pass

    def addUser(self,uid,uname,usex):
        url = host+'/adduser'
        data = {'uid':uid,'uname':uname,'usex':usex}
        print(data)
        res = requests.post(url=url,data=data)
        return res

    def selectAllUser(self):
        url = host + '/select'
        return requests.post(url=url)