#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :login.py
# @Time      :2023/7/27 22:57
# @Author    :Raink

import sys, time

from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5 import uic



def localtime():
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    return t


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.ui = uic.loadUi("./login1.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # 提取要操作的控件
        self.user_name_qwidget = self.ui.lineEdit  # 用户名输入框
        self.password_qwidget = self.ui.lineEdit_2  # 密码输入框
        self.login_btn = self.ui.pushButton  # 登录按钮
        self.forget_password_btn = self.ui.pushButton_2  # 忘记密码按钮
        self.page1_change_btn = self.ui.pushButton_3  # 画面切换1按钮
        self.page2_change_btn = self.ui.pushButton_4  # 画面切换2按钮
        self.textBrowser = self.ui.textBrowser  # 文本显示区域
        self.time_qwidget = self.ui.label_3 # 系统时间显示

        self.page_1 = self.ui.page_1  # 画面1
        self.page_1.show()
        self.page_2 = self.ui.page_2  # 画面2
        self.page_2.hide()

        # 绑定信号与槽函数
        self.login_btn.clicked.connect(self.login)

        self.page1_change_btn.clicked.connect(self.pagechange_1)
        self.page2_change_btn.clicked.connect(self.pagechange_2)

        # 实例化一个QTimer对象
        self.timer = QtCore.QTimer()
        # 绑定时间信号也槽函数
        self.timer.timeout.connect(self.showtime)
        self.timer.start(1000)


    def login(self):
        """登录按钮的槽函数"""
        user_name = self.user_name_qwidget.text()
        password = self.password_qwidget.text()
        if user_name == "admin" and password == "123456":
            self.textBrowser.setText("欢迎%s" % user_name)
            self.textBrowser.repaint()
        else:
            self.textBrowser.setText(f'{self.localtime}\n用户名或密码错误....请重试')
            self.textBrowser.repaint()
              
    def showtime(self):
        self.localtime = localtime()
        self.time_qwidget.setText(self.localtime)
        self.time_qwidget.repaint()

    def pagechange_1(self):
        self.page_1.show()
        self.page_2.hide()

    def pagechange_2(self):
        self.page_1.hide()
        self.page_2.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    # 展示窗口
    w.ui.show()

    app.exec()

