clientes = []

for i in range(3):
    print()
    cliente = {}
    cliente["nome"] = input("Digite seu nome: ")
    cliente["telefone"] = input("Digite seu numero de telefone: ")
    cliente["email"] = input("Digite seu E-mail: ")
    cliente["profissao"] = input("Digite sua profissão: ")
    print()

    clientes.append(cliente)


for cliente in clientes:
    print(cliente)