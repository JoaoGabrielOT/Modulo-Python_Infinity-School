# fazer um algoritmo que roda em looping infinito
usuarios = []
loop = True


def MostrarUsuarios():
    print()
    for i in usuarios:
        print(f"{usuarios.index(i)}: {i}")
    print()

while loop:
    print("""
          
1.Cadastrar usuario
2.Atualizar usuario
3.Deletar usuario
4.Listar usuarios
q.Sair
          
""")
    opcao = input("\nEscolha uma opção: ")
    match opcao.lower():
        case "1":
            nome = input("\nDigite o nome a ser cadastrado: ")
            usuarios.append(nome)

        case "2":
            MostrarUsuarios()
            usuarioAtualizar = int(input("\nDigite o numero do usuario que deseja atualizar: "))
            nome = input("\nDigite o nome a ser cadastrado: ")
            usuarios[usuarioAtualizar] = nome
            
        case "3":
            MostrarUsuarios()
            usuarioDeletar = int(input("\nDigite o numero do usuario que deseja deletar: "))
            usuarios.pop(usuarioDeletar)

        case "4":
            MostrarUsuarios()
        
        case "q":
            loop = False

        case _:
            print("opção invalida!")