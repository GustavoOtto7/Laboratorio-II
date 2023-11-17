from menu import principal_menu
from list_colors import colors, print_colored


def main():
    opc = principal_menu()
    if opc == 1:
        x = 1
    elif opc == 2:
        x = 2
    elif opc == 3:
        x = 3
    else:
        print_colored("Erro!", colors.red, colors.negative)
main()