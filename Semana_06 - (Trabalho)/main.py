from estoque import add_product, find_product_category, show_stock, change_product_value, remover_product
from vendas import sale_product, sales_report
from menuzao import show_menu
        
def main():
    stock = {}
    sales_dict = {}
    vendas = []
    while True:
        opc = show_menu()
        if opc == 1:
            while True:
                stock = add_product(stock)
                if input("Deseja adicionar outro produto? (s/n): ").lower() != "s":
                    break
        elif opc == 2:
            stock = change_product_value(stock)
        elif opc == 3:
            stock = remover_product(stock)
        elif opc == 4:
            find_product_category(stock)
        elif opc == 5:
            show_stock(stock)
        elif opc == 6:
            while True:
                stock = sale_product(stock, sales_dict)
                if input("Deseja vender outro produto? (s/n): ").lower() != "s":
                    break
        elif opc == 7:
            sales_report(sales_dict)
main()