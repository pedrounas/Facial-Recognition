import os
import sys


def get_students():

    path = './test/'
    files = os.listdir(path)
    names = []

    for file in files:
        if file.endswith('.jpg'):
            temp = file.split('.')[0]
            names.append(temp.replace("_", " "))

    with open('./students.txt', 'w+') as fp:
        for name in names:
            fp.write(name + '\n')
