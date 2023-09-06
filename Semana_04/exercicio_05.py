def verify(text):
    vowel = {'a' : 0,
             'e' : 0,
             'i' : 0,
             'o' : 0,
             'u' : 0}
    for letter in text:
        if letter in vowel:
            vowel[letter] += 1
    return vowel

def main():
    text = input("Digite seu texto: ")
    vowel = verify(text)
    print("Lista de repetições: ")
    for letter in vowel:
        for i in letter:
            print(f"Resultado {letter}: -> {vowel[i]}")
main()