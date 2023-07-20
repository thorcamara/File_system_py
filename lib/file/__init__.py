from lib.interface import *


def fileExists(name):
    try:
        f = open(name, 'rt')
        f.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createFile(name):
    try:
        f = open(name, 'wt+')
        f.close()
    except:
        print('There was an error creating the file!')
    else:
        print(f'File {name} successfully created!')


def readFile(name):
    try:
        f = open(name, 'rt')
    except:
        print('Error reading file!')
    else:
        header('Registered people')
        for line in f:
            data = line.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<30}{data[1]:>3} years')
    finally:
        f.close()


def register(file, name='unknown', age=0):
    try:
        f = open(file, 'at')
    except:
        print('There was an error opening the file!')
    else:
        try:
            f.write(f'{name};{age}\n')
        except:
            print('There was an error when writing the data!')
        else:
            print(f'New register of {name} added.')
            f.close()

