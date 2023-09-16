def sale_product(stock, sales_dict):
    """Venda de um produto."""
    product_name = input("Digite o nome do produto vendido: ")
    if product_name in stock:
        
        quantity_sold = int(input("Digite a quantidade de venda:"))
        currently_amount = stock[product_name]["amount"]
        if quantity_sold <= currently_amount:
            price = stock[product_name]["price"]
            sale_value = price * quantity_sold

         
    return stock

def sales_report(sales_dict):
        """Relatório de vendas."""
        index = 0
        for product_name in sales_dict.keys():
            index += 1
            quantity_sold = sales_dict[product_name]["quantidade_amount"]
            sale_value = sales_dict[product_name]["valor_price"]
            print(f"Venda - {index}: Produto: {product_name} Quantidade vendida: {quantity_sold} No valor total de: R${sale_value}")
      