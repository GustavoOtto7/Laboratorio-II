class colors:
    negative = 7
    white = 30
    red = 31
    green = 32
    invisible = 37
    back_color = 40
    back_gray = 47

def print_colored(message, code, code2 = None):
    print(f'\033[{code};{code2}m{message}\033[0m')
'''print_colored("Isso é pra ficar vermelho!", colors.red, colors.back_color)
print_colored("Isso é pra ficar verde!", colors.green, colors.back_gray)
print_colored("Isso é pra sumir!", colors.white, colors.negative)'''