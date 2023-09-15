def sale_product(stock, sales_dict):
    """Venda de um produto."""
    product_name = input("Digite o nome do produto vendido: ")
    quantity_sold = int(input("Digite a quantidade vendida: "))
    if product_name in stock:
        product = stock[product_name]
        current_quantity = product['amount']
        if quantity_sold <= current_quantity:
            product['amount'] -= quantity_sold
            sale_value = quantity_sold * product['price']
            if stock[product_name]['amount'] == 0:
                stock.pop(product_name)
            print(f"Venda realizada com sucesso! Valor total: R$ {sale_value}")
            sales_dict[product_name] = {"quantidade_amount": quantity_sold, "valor_price": sale_value}
        else:
            print("Quantidade em estoque insuficiente.")
    else:
        print("Produto não encontrado no estoque.")
    return stock

def sales_report(sales_dict):
        """Relatório de vendas."""
        index = 0
        for product_name in sales_dict.keys():
            index += 1
            quantity_sold = sales_dict[product_name]["quantidade_amount"]
            sale_value = sales_dict[product_name]["valor_price"]
            print(f"Venda - {index}: Produto: {product_name} Quantidade vendida: {quantity_sold} No valor total de: R${sale_value}")
      