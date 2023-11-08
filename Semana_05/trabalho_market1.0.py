def menu():
    print("## MERCADINHO DO SEU ZÉ ##")
    print("1- Adicionar um produto: ")
    print("2- Buscar um produto: ")
    print("3- Vizualizar todos os produtos: ")
    print("4- Vender um produto: ")
    print("5- Relatório de vendas: ")
    opc = int(input("O que você deseja? "))
    return opc

def add_product(stock):
    product = input("Digite o nome do produto: ")
    quant_in_stock = int(input("Digite a quantidade do produto: "))
    price = float(input("Digite o preço do produto: "))
        
    stock[product] = {
      "Quantidade:": quant_in_stock,
      "Valor": price
    }
    return stock
''' else:
        print("Você já possui esse produto!")
        quant = int(input("Digite a quantidade que será incrementada ao estoque: "))
        quant_in_stock += quant'''
    

def main():
    stock = {}
    opc = 0
    while opc != 6:
        opc = menu()
        if opc == 1:
            stock = add_product(stock)
            print(stock)

    print("Você saiu!")

main()
