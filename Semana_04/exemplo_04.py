def verify(list):
    dict = {}
    for i in list:
        #dict[i] = dict.get[number, 0] + 1
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

def main():
    list = "joao"
    dict = verify(list)
    print("Lista de repetições: ")
    print("Resultado: -> ", dict)

main()