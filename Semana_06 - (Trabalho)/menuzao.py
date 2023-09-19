def show_menu():
    """Menu de Opções"""
    print(30*'-_')
    print("##  MERCADINHO DO SEU ZÉ ##")
    print("1 - Adicionar um produto: ")
    print("2 - Alterar valor de um Produto: ")
    print("3 - Remover um produto: ")
    print("4 - Buscar um produto: ")
    print("5 - Historia de Estoque: ")
    print("6 - Vizualizar todos os produtos: ")
    print("7 - Vender um produto: ")
    print("8 - Relatório de vendas: ")
    print(30*'-_')
    opc = int(input("O que você deseja? "))
    return opc