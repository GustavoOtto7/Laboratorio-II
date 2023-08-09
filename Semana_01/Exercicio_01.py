def saldo_inicial():
    saldo = input(float("Digite seu saldo atual: "))
    return saldo

def menu():
    print("1- mostrar saldo atual: ")
    print("2- depositar")
    print("3- sacar")
    print("4- sair")

def escolha():
    opc = input(int("Digite a opção desejada: "))
    return opc

def mostrar_saldo(saldo):
    print("Seu saldo atual é de: ", saldo)

def deposito(saldo, depositos_efetuados):
    valor = input(float("Digite o valor do depósito: "))
    saldo = saldo + valor
    depositos_efetuados.append(valor)
    return saldo, depositos_efetuados 

def saque(saldo, saques_efetuados):
    valor = input(float("Digite o valor do saque: "))
    if saldo >= saque:
        saldo = saldo - saque
        saques_efetuados.append(valor)
    else:
        print("Saldo insuficiente!")
    return saldo, saques_efetuados
 
def main():
    depositos_efetuados = []
    saques_efetuados = []
    saldo = saldo_inicial()
    menu()
    opc = escolha()
    while opc != 4:
        if opc == 1:
            mostrar_saldo(saldo)
        elif opc == 2:
            deposito(saldo, depositos_efetuados)
        elif opc == 3:
            saque(saldo, saques_efetuados)
    print("Você saiu!")
    print("Depósitos efetuados: ", depositos_efetuados)
    print("Saques efetuados: ", saques_efetuados)
    
main()
