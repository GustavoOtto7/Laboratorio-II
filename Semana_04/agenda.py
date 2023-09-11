def menu():
    print("Selecione uma opção:")
    print("1- Criar novo contato:")
    print("2- Incluir telefone:")
    print("3- Remover um telefone:")
    print("4- Remover um contato:")
    print("5- Buscar um contato:")
    print("6- Listar contatos:")
    print("7- Sair")
    option = int(input("\nEscolha uma opção: "))
    return option

def add_contact(contacts, contact_name = None):
    if contact_name:
        name = contact_name
    else:
        name = input("Digite o nome do contato: ")
    contacts[name] = []
    while True:
        phone = input(f"> Digite um número para o contato {name}: ")
        if phone == "":
            break
        contacts[name].append(phone)

def include_phone(contacts):
    name = input("> Digite o nome do contato que você deseja incluir um telefone: ")
    if name in contacts:
        phone = input(f"> Digite um número para o contato {name}: ")
        contacts[name].append(phone)
    else: 
        print("Esse contato ainda não existe!")
        include_contact = input(f"O contato {name} ainda não existe. Deseja incluir? (S/N) ").upper()
        if include_contact == "S":
            add_contact(contacts, name)

def delete_phone(contacts):
    name = input("> DIgite o nome do contato que você deseja remover um número: ")
    if name in contacts:
        print("# Telefones")
        for index in range(len(contacts[name])):
            print(f" {index} --> {contacts[name][index]}")
        if len(contacts[name]) == 1:
            contacts.pop(name)
            print("O contato possuia aoenas um número e foi removido da lista.")
            return
        remove_index = int(input("Qual número você deseja remover? "))
        contacts[name].pop(remove_index)
    else:
        print(f"O contato {name} não existe!")

def delete_contact(contacts):
    name = input("Digite o nome que você deseja remover: ")
    if name in contacts:
        contacts.pop(name)
    else:
        print(f'O contato {name} não existe')

def find_contact(contacts):
    name = input("> Digite o nome do contato: ")
    if name in contacts:
        print("# Telefones:")
        for phone in contacts[name]:
            print(f"> {phone}")
    else:
        print(f"O contato {name} não existe.")

def main():
    contacts = {}
    while True:
        option = menu()
        if option == 1:
            print("Adicionar novo contato: ")
            add_contact(contacts)
        elif option == 2:
            include_phone(contacts)
        elif option == 3:
            delete_phone(contacts)
        elif option == 4:
            delete_contact(contacts)
        elif option == 5:
            find_contact(contacts)
        elif option == 6:
            print(contacts)
        elif option == 7:
            print("Você saiu!")
            print("Contatos: ", contacts)
            break
main()