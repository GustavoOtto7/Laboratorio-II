def verify(text):
    alfhabet = {}
    for letter in text:
        if letter not in alfhabet:
            alfhabet[letter] = 1
        elif letter in alfhabet:
            alfhabet[letter] += 1
    return alfhabet

def main():
    text = input("Digite seu texto: ")
    alfhabet = verify(text)
    print("Lista de repetições: ")
    for letter in alfhabet:
        for i in letter:
            print(f"Resultado {letter}: -> {alfhabet[i]}")
main()