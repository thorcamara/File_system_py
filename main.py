from lib.interface import *
from lib.file import *
from time import sleep

file = 'file.txt'

if not fileExists(file):
    createFile(file)


while True:
    answer = menu(['See registered people', 'Register new person', 'Exit the system'])
    if answer == 1:
        readFile(file)
    elif answer == 2:
        header('New register')
        name = str(input('Name: '))
        age = readInt('Age: ')
        register(file, name, age)
    elif answer == 3:
        header('Exiting the system... see you later')
        break
    else:
        print('\033[31mERROR! Type a valid option!\033[m')
    sleep(1)