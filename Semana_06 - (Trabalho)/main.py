from estoque import add_product, find_product, show_stock
from vendas import sale_product, sales_report
from menuzao import show_menu

def main():
    stock = {}
    sales_dict = {}
    opc = 0
    while opc <= 5:
        opc = show_menu()
        if opc == 1:
            while True:
                stock = add_product(stock)
                if input("Deseja adicionar outro produto? (s/n): ").lower() != "s":
                    break
        elif opc == 2:
            find_product(stock)
        elif opc == 3:
            show_stock(stock)
        elif opc == 4:
            while True:
                stock = sale_product(stock, sales_dict)
                if input("Deseja vender outro produto? (s/n): ").lower() != "s":
                    break
        elif opc == 5:
            sales_report(sales_dict)
    print("Você saiu!")
main()