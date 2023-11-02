def menu():
    while True:
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
    while True:
        try:
            value = float(input("Digite o valor que você deseja depositar: "))
            if value > 0:
                bank_account["balance"] += value
                bank_account["historic"].append(f"Depositados R$ {value}")
                print("Depósito realizado com sucesso!")
                return bank_account
            else:
                print("Você precisa digitar um valor positivo!")
        except ValueError:
            print("Você precisa digitar um valor válido!")    
        except BaseException as error:
            print(f"[Erro] - {error}")

def withdraw(bank_account):
    while True:
        try:
            value = float(input("Digite o valor que você deseja sacar: "))
            if value > 0 and value <= bank_account["transaction_limit"]:
                if value <= bank_account["balance"]:
                    bank_account["balance"] -= value
                    bank_account["historic"].append(f"Sacados R$ {value}")
                    print("Saque realizado com sucesso!")
                    return bank_account
                else:
                    print("Seu saldo é insuficiente!")
            else:
                print("Você precisa digitar um valor positivo ou o valor ultrapassou o saque limite!")
        except ValueError:
            print("Você precisa digitar um valor válido!")
        except BaseException as error:
            print(f"[Erro] - {error}")

def show_balance(bank_account):
    print(f'Seu saldo bancário atual é de: {bank_account["balance"]}')

def show_historic(bank_account):
    for i, alt in enumerate(bank_account["historic"]):
        print(f'Seu histórico de alterações: {i + 1} - {alt}')

def main():
    bank_account = {
        "balance" : 3000,
        "transaction_limit" : 1000,
        "historic" : []}
    try:
        opc = menu()
        while opc < 6:
            if opc == 1:
                bank_account = deposit(bank_account)
                opc = menu()
            elif opc == 2:
                bank_account = withdraw(bank_account)
                opc = menu()
            elif opc == 3:
                show_balance(bank_account)
                opc = menu()
            elif opc == 4:
                show_historic(bank_account)
                opc = menu()
            elif opc >= 5:
                print("Você saiu!")
                break
    except ValueError:
        print("Você precisa digitar um valor válido!")               
    except BaseException as error:
        print(f"[Erro] - {error}")
main()