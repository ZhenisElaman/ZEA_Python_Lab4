#!/usr/bin/env python3
# coding=utf-8

import sys

from random import randint
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


# Основной класс программы
class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('Form.ui', self)  # Загрузка формы из файла

        # Задание заголовка окна
        self.setWindowTitle('Разработка кроссплатформенных приложений')

        self.pushButton_run.clicked.connect(self.run)
        self.pushButton_random.clicked.connect(self.random)


    def random(self):
        row = 0
        col = 0
        while row < self.tableWidget_array.rowCount():
            while col < self.tableWidget_array.columnCount():
                random_num = randint(0, 100)
                self.tableWidget_array.setItem(row, col, QTableWidgetItem(str(random_num)))
                col += 1
            row += 1
            col = 0


    def run(self):
        fm = self.find_max()

        zero_count = self.find_zero_count()

        self.label_max.setText(
                'Максимальный элемент: ' + str(fm[0]) + ' [' + str(fm[1]) + ', 2]')
        self.label_zero.setText(
                'Кол-во нулей во 2 строке: ' + str(zero_count))
        self.tableWidget_array.setItem(fm[1], 1, QTableWidgetItem(str(zero_count)))


    def find_max(self):
        pos_max = 0
        max_num = 0
        row = 0
        try:
            while row < self.tableWidget_array.rowCount():
                number = float(self.tableWidget_array.item(row, 1).text())
                if number > max_num:
                    max_num = number
                    pos_max = row
                row += 1
            return [max_num, pos_max]
        except Exception:
            return None


    def find_zero_count(self):
        col = 0
        zero_count = 0
        while col < self.tableWidget_array.columnCount():
            number = float(self.tableWidget_array.item(1, col).text())
            if number == 0:
                zero_count += 1
            col += 1
        return zero_count


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()