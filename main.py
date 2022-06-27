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
