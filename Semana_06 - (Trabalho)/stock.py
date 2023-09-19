def add_product(stock):
    """Adiconar/Verificar um Produto ao Estoque"""
    product_name = input("Digite o nome do produto: ")
    if product_name == '':
        return
    if product_name in stock:
        temp_quantity = int(input("Digite a quantidade do produto: "))
        stock[product_name]["amount"] += temp_quantity
    else:
        product_amount = int(input("Digite a quantidade do produto: "))
        product_price = float(input("Digite o preço do produto: R$"))
        product_category = input("Digite uma Categoria: ")
        stock[product_name] = {
            "amount": product_amount,
            "price": product_price,
            "category": product_category}
        
    for product_name, product_info in stock.items():
        amount = product_info["amount"]
        price = product_info["price"]
        category = product_info["category"]
    print(f"O produto {product_name} foi adicionado com sucesso!")
    print(f"Produto: {product_name}, Quantidade: {amount}, Preço: {price}, Categoria: {category}")
    return stock

def change_product_value(stock, product_upgrade = None):
    """Alterar Valor de Produto"""
    product_upgrade = []
    product_name = input("Qual produto deseja mudar o valor ? ")
    if product_name in stock.keys():
        print(f"Procurando {product_name}")
        new_price = float(input("Digite novo valor: "))
        stock[product_name]["price"] = new_price
        print(f"Novo valor: {new_price}")
        product_upgrade.append(new_price)
        #print(product_upgrade)
    else:
        print(f"{product_name} não encontrado.")
    return stock, product_upgrade
        


    return stock
    
def find_product_category(stock):
    """Buscar produto no estoque / Categoria no Stock"""
    print("1 - Buscar por nome do Produto")
    print("2 - Buscar por categoria")
    print("3 - Sair")
    opc = int(input("Escolha uma opção: "))
    if opc == 1:
        product_name = input("Digite o nome do Produto: ")
        if product_name in stock:
            print(f"Procurando {product_name}...")
            
            amount = stock[product_name]["amount"]
            price = stock[product_name]["price"]
            category = stock[product_name]["category"]

            print(f"Produto: {product_name}")
            print(f"Quantidade: {amount}") 
            print(f"Preço: {price}")
            print(f"Categoria: {category}")
        else:
            print(f"Produto {product_name} não registrado")
    elif opc == 2:
        product_category = input("Digite a categoria: ")

        for product in stock.values():
            if product['category'] == product_category:
                print(product)      
            else:
                print(f"Categoria não encontrada.")
                return
    elif opc == 3:
        return

def remover_product(stock, product_remove_lista = None):
    """Remover Produto"""
    product_remove_lista = []
    product_name = input("Digite o produto que deseja remover: ")
    if product_name in stock.keys():
        print(f"Procurando {product_name}...")
        product_remove = stock[product_name]
        product_remove_lista.append(product_remove)
        stock.pop(product_name)
        print(f"{product_remove} removido com sucesso!")
    else:
        print(f"{product_remove} não encontrado.")
    #print(product_remove_lista)
    #print(stock)
    return stock, product_remove_lista
        
def show_stock(stock, product_remove_lista = None, product_upgrade = None):
    """Mostrar completamente o estoque"""
    for product_name, product_info in stock.items():
        amount = product_info["amount"]
        price = product_info["price"]
        category = product_info["category"]
        print(f"Produto: {product_name}, Quantidade: {amount}, Preço: {price}, Categoria: {category}")
        if product_remove_lista is not None:
            for remove in product_remove_lista:
                print(f"Produto Removido:{product_name} {remove}")
        if product_upgrade is not None:
            for upgrade in product_upgrade:
                print(f"Produto Atualizado: {product_name}, Novo Valor: {upgrade}")