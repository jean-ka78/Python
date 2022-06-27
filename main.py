# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import numpy as np
import os
import glob
import time
import django as dj
import pandas as pd
import random as rd

# animals = ['cat', 'dog', 'giraffe']
# print(animals[2])
# os.system('modprobe wl-gpio' )
# os.system('modprobe w1-therm')
localtime = time.localtime(time.time())
sec = localtime.tm_sec
print("Local current time :", sec)


class Parrot:
    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")


class Penguin:
    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")


def flying_test(bird):
    bird.swim()
    bird.fly()


blu = Parrot()
peggy = Penguin()

flying_test(peggy)
flying_test(blu)
# import socket
# from pyModbusTCP.client import ModbusClient
t = rd.randrange(-50.00, 15.00)
print('Number: ', t)
