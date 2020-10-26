#!/usr/bin/env python3
# -*- config: utf-8 -*-

# Вариант 3
# Дано предложение. Вывести все буквы м и н в нем.
if __name__ == '__main__':
    p = input("Введите предложение: ")

    for m in p:
        if m == 'м':
            print(f"{m}")
    for n in p:
        if n == 'н':
            print(f"{n}")