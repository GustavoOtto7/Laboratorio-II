def shopping():
    buy_list = {}
    while True: 
        answer = str(input("Quer adicionar um produto: S/N  ")).upper()
        if answer == "N":
            return buy_list
        product_name = input("Digite o nome do produto: ")
        quantity = int(input("Digite a quantidade: "))

        if product_name in buy_list:
            buy_list[product_name] += quantity
        else:  
            buy_list[product_name] = quantity    

def main():
    buy_list = shopping()
    print("Sua lista de compras: ", buy_list)
main()