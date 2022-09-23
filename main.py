#!/usr/bin/env python3
# coding=utf-8

import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

# Основной класс программы
class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('Form1.ui', self)  # Загрузка формы из файла

        # Задание заголовка окна
        self.setWindowTitle('Разработка кроссплатформенных приложений')

        # Задание картинки с заданием с масштабированием в компоненте
        self.label_img.setPixmap(QPixmap('task.png'))
        self.label_img.setScaledContents(True)

        # Привязываем к кнопкам наши процедуры-обработчики
        self.pushButton_Run.clicked.connect(self.solve)
        self.pushButton_Clean.clicked.connect(self.clean)

    # Процедура решения примера
    def solve(self):
        try:
            A = int(self.lineEdit_A.text())
            B = int(self.lineEdit_B.text())
            X = int(self.lineEdit_X.text())
            try:
                if (X < 7):
                    y = ((pow(X, 2) + pow(A, 2) + pow(B, 2)) / (A + B))
                else:
                    y = pow(X, 3) * pow((A + B), 2)
                self.label_Answer.setText('Y = ' + str(format(y, '.2f')))
                self.label_Answer.setStyleSheet("QLabel { background-color: green;"
                                                "color: white;}")
            except:
                self.label_Answer.setText('Нет ответа!')
                self.label_Answer.setStyleSheet("QLabel { background-color: red;"
                                                "color: white;}")
        except:
            self.label_Answer.setText('Неверные входные данные')
            self.label_Answer.setStyleSheet("QLabel { background-color: red;"
                                            "color: white;}")

    def clean(self):
        self.lineEdit_A.setText('')
        self.lineEdit_B.setText('')
        self.lineEdit_X.setText('')
        self.label_Answer.setText('Y = ')

# Основная часть программы
app = QApplication(sys.argv)
window = Main()  # базовый класс окна
window.show()  # отобразить окно на экране
sys.exit(app.exec_())  # запуск основного цикла приложения
