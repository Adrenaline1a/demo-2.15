#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
В данном упражнении вы должны написать программу, которая будет находить самое
длинное слово в файле. В качестве результата программа
должна выводить на экран длину самого длинного слова и все слова такой длины. Для
простоты принимайте за значимые буквы любые непробельные символы, включая цифры и
знаки препинания.
"""


if __name__ == "__main__":
    with open("ind2.txt", "r", encoding='utf-8') as f:
        words = []
        count = 0
        file = (f.read()).split(' ')
        for w in file:
            length = len(w)
            if length > count:
                count = length
        for w in file:
            if len(w) == count:
                words.append(w)
        print('Максимальная длина слова в файле: ', count)
        print('Самые длинные слова в файле:', " ".join(words))
