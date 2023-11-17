def print_colorido(texto, cor):
    cores = {
        'reset': '\033[0m',
        'preto': '\033[30m',
        'vermelho': '\033[31m',
        'verde': '\033[32m',
        'amarelo': '\033[33m',
        'azul': '\033[34m',
        'magenta': '\033[35m',
        'ciano': '\033[36m',
        'branco': '\033[37m',
    }

    if cor not in cores:
        cor = 'reset'

    print(cores[cor] + texto)

# Exemplo de uso
print_colorido("Esta palavra é vermelha.", 'vermelho')
print_colorido("Esta palavra é verde.", 'verde')
