class colors:
    normal = 1
    negative = 7
    white = 30
    red = 31
    green = 32
    yellow = 33
    invisible = 37
    back_color = 40
    back_gray = 47

def print_colored(message, code, code2 = 1):
    print(f'\033[{code};{code2}m{message}\033[0m')

def add_colored(message, code, code2 = 1):
    return f'\033[{code};{code2}m{message}\033[0m'