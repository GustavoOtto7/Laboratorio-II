def menu():
    print("## MERCADINHO DO SEU ZÉ ##")
    print("1- Adicionar um produto: ")
    print("2- Buscar um produto: ")
    print("3- Vizualizar todos os produtos: ")
    print("4- Vender um produto: ")
    print("5- Relatório de vendas: ")
    opc = int(input("O que você deseja? "))
    return opc

def adicionar_produto(stock):
    product_name = input("Digite o nome do produto: ")
    if product_name == '':
        return
    elif product_name in stock.keys():
        temp_quantity = int(input("Digite a quantidade do produto: "))
        stock["amount"][product_amount] = sum(temp_quantity + stock["amount"][product_amount])
    else:
        product_amount = int(input("Digite a quantidade do produto: "))
        product_price = float(input("Digite o preço do produto: R$"))
    stock[product_name] = {
      "amount": product_amount,
      "price": product_price}
    for product_name, product_info in stock.items():
        amount = product_info["amount"]
        price = product_info["price"]
    print(f"O produto {product_name} foi adicionado com sucesso!")
    print(f"Produto: {product_name}, Quantidade: {amount}, Preço: {price}")
    return stock
    

def buscar_produto(stock):
    product_name = input("Digite o nome do Produto: ")
    if product_name in stock:
        print(f"Procurando {product_name}...")
        for amount, price in stock[product_name].items():
            amount = stock[product_name]["amount"]
            price = stock[product_name]["price"]
        print(f"Produto: {product_name}, Quantidade: {amount}, Preço: {price}")
    else:
        print(f"Produto {product_name} não registrado")

def produto_estoque(stock):
    for product_name, product_info in stock.items():
        amount = product_info["amount"]
        price = product_info["price"]
        print(f"Produto: {product_name}, Quantidade: {amount}, Preço: {price}")

def venda_produto(stock, sales_dict):
    product_name = input("Digite o nome do produto vendido: ")
    quantity_sold = int(input("Digite a quantidade vendida: "))
    if product_name in stock:
        product = stock[product_name]
        current_quantity = product['amount']
        if quantity_sold <= current_quantity:
            product['amount'] -= quantity_sold
            sale_value = quantity_sold * product['price']
            print(f"Venda realizada com sucesso! Valor total: R$ {sale_value}")
            sales_dict[product_name] = {"quantidade_amount": quantity_sold, 
                                        "valor_price": sale_value}
        else:
            print("Quantidade em estoque insuficiente.")
    else:
        print("Produto não encontrado no estoque.")

def sales_report(sales_dict):
        index = 0
        for product_name in sales_dict.keys():
            index += 1
            quantity_sold = sales_dict[product_name]["quantidade_amount"]
            sale_value = sales_dict[product_name]["valor_price"]
            print(f"Venda - {index}: Produto: {product_name} Quantidade vendida: {quantity_sold} No valor total de: R${sale_value}")
        
def main():
    stock = {}
    sales_dict = {}
    while True:
        opc = menu()
        if opc == 1:
            while True:
                adicionar_produto(stock)
                if input("Deseja adicionar outro produto? (s/n): ").lower() != "s":
                    break
        elif opc == 2:
            buscar_produto(stock)
        elif opc == 3:
            produto_estoque(stock)
        elif opc == 4:
            while True:
                venda_produto(stock, sales_dict)
                if input("Deseja vender outro produto? (s/n): ").lower() != "s":
                    break
        elif opc == 5:
            sales_report(sales_dict)
main()
#retirar o produto quando seu estoque for zero