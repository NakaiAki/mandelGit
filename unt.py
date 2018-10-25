# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 12:40:46 2018

@author: 章人
"""
from PyQt5 import QtGui as Qg, QtWidgets as Qw, QtCore as Qt

import sys
import untitled


class MyForm(Qw.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = untitled.Ui_MainWindow()
        self.ui.setupUi(self)

    def start(self):
        pass


if __name__ == '__main__':
    app = Qw.QApplication(sys.argv)  # パラメータは正しくはコマンドライン引数を与える
    wmain = MyForm()  # MyFormのインスタンスを作って
    wmain.show()  # 表示する
    sys.exit(app.exec())
