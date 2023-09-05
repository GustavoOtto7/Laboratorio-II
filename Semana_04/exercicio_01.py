def search():
    pessoas = {'Ana' : 'branca',
        'Carlos' : 'preta',
        'Clara' : 'rosa',
        'Luan' : 'azul',
        'Bruno' : 'vermelha'}
    return pessoas

def main():
    pessoas = search()
    for k, v in pessoas.items():
        print(f"A cor da camisa de {k} é {v}!")
main()