#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


"""Напишите программу, которая будет выполнять действия над файлами/каталогами
 в виде: “команда” “наименование файла/каталога”."""


if __name__ == "__main__":
    while True:
        message = input("Введите команду: ").lower()
        task = message.split(' ')
        if message.startswith("mkdir "):
            os.mkdir(task[1])
        elif message.startswith("rmdir "):
            os.rmdir(task[1])
        elif message.startswith("create "):
            open(task[1], 'w')
        elif message.startswith("remove "):
            os.remove(task[1])
        elif message.startswith("rename "):
            os.rename(task[1], task[2])
        elif message.startswith("exit"):
            exit()
        elif message.startswith("open "):
            os.system(f"notepad.exe {task[1]}")
        else:
            print("Неизвестная команда")
