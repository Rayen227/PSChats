import sys
from scripts import  index
from db import dbmanager
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # MainWindow = QMainWindow()
    # ui= index.MainWindowController(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())

    # 测试数据库链接
    dbm = dbmanager.DBManager()
    # res = dbm.addUser('2111220001','test01','男')
    res = dbm.selectAllUser()
    print(res.content.decode('utf-8'))
