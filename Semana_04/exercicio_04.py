def verify(pets):
    print("Chaves: gato, cachorro, coelho, pássaro")
    name = str(input("Digite um animal para verificar:  " )).lower()
    if name in pets:
        print("Verdadeiro! O animal está nas chaves!")
    else:
        print("Falso! Não está!")

def main():
    pets = {'gato' : 'Garfield',
        'cachorro' : 'Salsicha',
        'coelho' : 'Rabbit',
        'pássaro' : 'Andorinha',}
    verify(pets)
main()