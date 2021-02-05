# encoding: utf-8
"""
@version: 1.0
@author: Jarrett
@file: CNKIdownloader
@time: 2020/2/21 22:40
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


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("mainwidow.ui", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())