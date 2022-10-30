import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    # 设置窗口标题
    w.setWindowTitle("Hello PyQt5")
    # 展示窗口
    w.show()
    # 程序进入循环等待状态
    app.exec()

