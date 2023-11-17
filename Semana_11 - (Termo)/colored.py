class colored:
    reset = '\033[0m'
    negative = '\033[7m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    white = '\033[37m'
    back_color ='\033[40m'
    back_gray = '\033[47m'

class ImpressoraColorida:
    @staticmethod
    def imprimir_texto_colorido(texto, colored):
        cor_formatada = getattr(colored, cor, colored.reset)
        print(f"{cor_formatada}Erro{colored.reset}", 'Continua normal')

cor = colored
impressora = ImpressoraColorida()
impressora.imprimir_texto_colorido("vermelho", red)