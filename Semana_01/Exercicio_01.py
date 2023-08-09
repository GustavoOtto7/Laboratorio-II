def saldo_inicial():
    saldo = float(input("Digite seu saldo atual: "))
    return saldo

def menu():
    print("1- mostrar saldo atual: ")
    print("2- depositar")
    print("3- sacar")
    print("4- sair")

def escolha():
    opc = int(input("Digite a opção desejada: "))
    return opc

def mostrar_saldo(saldo):
    print("Seu saldo atual é de: ", saldo)
    
def deposito(saldo, depositos_efetuados):
    valor = float(input("Digite o valor do depósito: "))
    saldo = saldo + valor
    depositos_efetuados.append(valor)
    return saldo, depositos_efetuados 

def saque(saldo, saques_efetuados):
    valor = float(input("Digite o valor do saque: "))
    if saldo >= valor:
        saldo = saldo - valor
        saques_efetuados.append(valor)
    else:
        print("Saldo insuficiente!")
    return saldo, saques_efetuados
 
def main():
    saldo = saldo_inicial()
    menu()
    depositos_efetuados = []
    saques_efetuados = []
    opc = escolha()
    while opc != 4:
        if opc == 1:
            mostrar_saldo(saldo)
            opc = escolha()
        elif opc == 2:
            saldo, depositos_efetuados = deposito(saldo, depositos_efetuados)
            opc = escolha()
        elif opc == 3:
            saldo, saques_efetuados = saque(saldo, saques_efetuados)
            opc = escolha()
    print("Você saiu!")
    print("Depósitos efetuados: ", depositos_efetuados)
    print("Saques efetuados: ", saques_efetuados)
    
main()
