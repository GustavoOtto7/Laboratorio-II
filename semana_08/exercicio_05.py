def menu():
    print('''BANCO - Opções:
          1 - Depositar
          2 - Sacar
          3 - Verificar Saldo
          4 - Histórico de movimentações
          5 - Sair''')
    try:
        opc = int(input("Digite a opção desejada: "))
        return opc
    except ValueError:
        print("Você precisa digitar um valor válido!")    
    except BaseException as error:
        print(f"[Erro] - {error}")

def deposit(bank_account):
    try:
        value = float(input("Digite o valor que você deseja depositar: "))
        if value > 0:
            bank_account["balance"] += value
            bank_account["historic"].append(f"Depositados R$ {value}")
            return bank_account
        else:
            print("Você precisa digitar um valor positivo!")
            deposit(bank_account)
    except ValueError:
        print("Você precisa digitar um valor válido!")    
    except BaseException as error:
        print(f"[Erro] - {error}")

def withdraw(bank_account):



def show_balance(bank_account):



def show_historic(bank_account):


def go_out():



def main():
    bank_acount ={
        "balance" : 3000,
        "transaction_limit" : 1000,
        "historic" : []
    }
    try:
        opc = menu()
        while opc != 5:
            if opc == 1:

            elif opc == 2:

            elif opc == 3:

            elif opc == 4:

            elif opc > 5:


    except ValueError:
        print("Você precisa digitar um valor válido!")               
    except BaseException as error:
        print(f"[Erro] - {error}")

main()