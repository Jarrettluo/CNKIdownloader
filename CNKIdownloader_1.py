# encoding: utf-8
"""
@version: 1.0
@author: 
@file: CNKIdownloader_1
@time: 2020/2/22 13:42
"""

import time, sys, os
"""
以下引用是由于使用PyInstaller进行软件打包时出现bug。
参考链接：https://bbs.csdn.net/topics/392428917
"""
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']

from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QAction

from SendEmail.sendemail import *
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("window_v1.0.ui", self)
        self.setWindowTitle('CNKI文章下载器')
        self.title = ""
        self.EmailAddr = ""
        self.init_UI()
        self.lineEdit.textChanged.connect(self.setting)
        self.lineEdit_2.textChanged.connect(self.setting)
        self.pushButton.clicked.connect(lambda :self.Sending(self.title,self.EmailAddr))

    def init_UI(self):
        str = self.lineEdit.text()
        if str == "":
            self.pushButton.setEnabled(False)
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")

    def setting(self):
        self.title = self.lineEdit.text()
        self.EmailAddr = self.lineEdit_2.text()
        if self.title and self.EmailAddr:
            self.pushButton.setEnabled(True)

    def Sending(self, title, EmaiAddr):

        CNKI_file_name = "微信图片_20200221221814.jpg"

        title = "heheh"
        msg = "测-试-测-试"
        receivers = "luojiarui2@163.com"
        file = CNKI_file_name

        automail(title, msg, receivers, file)

        #str = 'heheh'
        print("ffsfs")
        self.pushButton.setEnabled(False)
        self.lineEdit.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.statusBar().showMessage("正在发送中，请等待")
        #self.pushButton.setText("发送中")
        self.init_UI()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())