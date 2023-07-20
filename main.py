from lib.interface import *
from time import sleep

while True:
    answer = menu(['See registered people', 'Register new person', 'Exit the system'])
    if answer == 1:
        header('Option 1')
    elif answer == 2:
        header('Option 2')
    elif answer == 3:
        header('Exiting the system... see you later')
        break
    else:
        print('\033[31mERROR! Type a valid option!\033[m')
    sleep(2)