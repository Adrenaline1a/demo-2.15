#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Написать программу, которая считывает текст из файла и выводит его на экран, меняя
местами каждые два соседних слова.
"""


if __name__ == "__main__":
    with open("ind1.txt", "r", encoding='utf-8') as f:
        file = (f.read()).split(' ')
        print('Содержимое файла:', ' '.join(file))
        try:
            for i, n in enumerate(file):
                if i % 2 == 0:
                    file[i], file[i + 1] = file[i + 1], file[i]
            print("После выполнения перестановки: ", ' '.join(file))
        except IndexError:
            print("После выполнения перестановки: ", ' '.join(file))
