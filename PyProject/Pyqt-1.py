import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QDesktopWidget, QVBoxLayout, \
    QGroupBox, QRadioButton, QHBoxLayout





class MyUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.center_display()

    def init_ui(self):
        # 设置窗口标题
        self.setWindowTitle("This is My PyQt!")
        self.setWindowIcon(QIcon('pic.png'))
        # 窗口大小
        self.resize(800, 600)

        # 最外层的垂直布局器，包含两个部分：爱好和性别
        container = QVBoxLayout()

        # --创建第一个分组，添加多个组件--
        # hobby 主要是保证他们是一个组
        hobby_box = QGroupBox('爱好')
        # 创建垂直布局器
        v_layout = QVBoxLayout()

        # 创建爱好按钮
        btn1 = QRadioButton('抽烟')
        btn2 = QRadioButton('喝酒')
        btn3 = QRadioButton('烫头')

        # 添加到v_layout中
        v_layout.addWidget(btn1)
        v_layout.addWidget(btn2)
        v_layout.addWidget(btn3)

        # 添加垂直布局器到爱好容器中
        hobby_box.setLayout(v_layout)

        # 创建性别容器
        gender_box = QGroupBox('性别')
        # 创建水平布局器
        h_layout = QHBoxLayout()
        # 添加性别按钮
        btn4 = QRadioButton('男')
        btn5 = QRadioButton('女')
        # 追加性别内容到水平布局器中
        h_layout.addWidget(btn4)
        h_layout.addWidget(btn5)

        # 添加水平布局到性别容器中
        gender_box.setLayout(h_layout)

        # 添加爱好的内容到容器中
        container.addWidget(hobby_box)
        # 添加性别的内容到容器中
        container.addWidget(gender_box)

        # 添加容器到MyUI布局
        self.setLayout(container)

    def center_display(self):
        # 获取可用屏幕中央位置的点坐标
        center_pointer = QDesktopWidget().availableGeometry().center()
        x = center_pointer.x()
        y = center_pointer.y()
        print(f'center_pointer{center_pointer}')
        # w.move(x, y)
        old_x, old_y, width, height = self.frameGeometry().getRect()
        print(f'w.frameGeometry().getRect() {self.frameGeometry().getRect()},{x - (width / 2), y - (height / 2)}')
        # 计算UI界面的中心点
        self.move(int(x - width / 2), int(y - height / 2))






# 调整窗口在屏幕中央 #todo


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # # 创建桌面应用的UI元素
    # w = QWidget()
    #
    # # 设置窗口标题
    # w.setWindowTitle("This is My PyQt!")
    # # 窗口大小
    # w.resize(800, 600)
    # # 调整窗口位置
    # # w.move(0, 0)
    # center_display()
    #
    # # 在窗口中添加元素
    # btn = QPushButton('登 录')
    # # 设置按钮的父窗口是当前窗口
    # btn.setParent(w)
    # btn.setGeometry(100, 100, 60, 30)
    #
    # # 创建一个标签
    # usrlabel = QLabel('账号：', w)
    # # usrlabel.setParent(w)
    #
    # pwdlabel = QLabel('密码：')
    # pwdlabel.setParent(w)
    #
    # # 显示位置与大小 setGeometry（X,Y,W,H)
    # usrlabel.setGeometry(20, 20, 30, 30)
    # pwdlabel.setGeometry(20, 60, 30, 30)
    #
    # # 创建文本框
    # usredit = QLineEdit(w)
    # usredit.setPlaceholderText('请输入用户名')
    # usredit.setGeometry(60, 20, 150, 30)
    #
    # pwdedit = QLineEdit(w)
    # pwdedit.setPlaceholderText('请输入密码')
    # pwdedit.setGeometry(60, 60, 150, 30)



    # 展示窗口
    w = MyUI()
    w.show()
    # 程序循环进行状态确认
    app.exec()