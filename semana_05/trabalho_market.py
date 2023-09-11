def menu():
    print("## MERCADINHO DO SEU ZÉ ##")
    print("1- Adicionar um produto: ")
    print("2- Buscar um produto: ")
    print("3- Vizualizar todos os produtos: ")
    print("4- Vender um produto: ")
    print("5- Relatório de vendas: ")
    opc = input("O que você deseja? ")
    return opc

def add_product(stock):
    if product not in stock:
        product = input("Digite o nome do produto: ")
        stock = product
        for product in stock:
            quant_in_stock = int(input("Digite a quantidade em estoque: "))
            price = float(input("Digite o preço do produto: "))
    return product, quant_in_stock, price
''' else:
        print("Você já possui esse produto!")
        quant = int(input("Digite a quantidade que será incrementada ao estoque: "))
        quant_in_stock += quant'''

    

def main():
    stock = {
        "product" : {"Quantidade" : quant_in_stock, "Valor" : price}}
    opc = menu()
    if opc == 1:
        product, quant_in_stock, price = add_product(stock)
        print(stock)

main()