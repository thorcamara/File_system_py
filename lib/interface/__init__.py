

def readInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERROR: please, type a valid Integer.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mUser chose not to enter this number/\033[m')
            return 0
        else:
            return n


def line(size=42):
    return '-' * size


def header(txt):
    print(line())
    print(txt.center(42))
    print(line())


def menu(list):
    header('Main menu')
    c = 1
    for item in list:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(line())
    option = readInt('\033[32mYour Option: \033[m')
    return option

