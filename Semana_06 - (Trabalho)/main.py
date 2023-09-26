from stock import add_product, find_product_category, show_stock, change_product_value, remover_product
from sale import sale_product, sales_report
from menuu import show_menu
        
def main():
    stock = {}
    sales_dict = {}
    product_remove_lista = []
    product_upgrade = []
    product_additions = []
    while True:
        opc = show_menu()
        if opc == 1:
            while True:
                stock, product_additions = add_product(stock, product_additions)
                if input("Deseja adicionar outro produto? (s/n): ").lower() != "s":
                    break
        elif opc == 2:
            stock, product_upgrade = change_product_value(stock, product_upgrade)
        elif opc == 3:
            stock, product_remove_lista = remover_product(stock, product_remove_lista)
        elif opc == 4:
            find_product_category(stock)
        elif opc == 5:
            show_stock(stock, product_remove_lista, product_upgrade, product_additions)
        elif opc == 6:
            while True:
                stock = sale_product(stock, sales_dict)
                if input("Deseja vender outro produto? (s/n): ").lower() != "s":
                    break
        elif opc == 7:
            sales_report(sales_dict)
main()