from lib.interface import *


def fileExists(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createFile(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('There was an error creating the file!')
    else:
        print(f'File {name} successfully created!')


def readFile(name):
    try:
        a = open(name, 'rt')
    except:
        print('Error reading file!')
    else:
        header('Registered people')
        print(a.read())