marte = ("Marte", "3.396km", "Fina e rarefeita")

alunos_e_notas = [("João", 10.0), ("Maria", 9.0), ("Vitoria", 8.0)]
for aluno in alunos_e_notas:
    print(aluno)

# ======================================================================
import random

clientes = []
loop = True
def mostrarClientes():
    if clientes:
        print("\nLista atual:")
        for i, cliente in enumerate(clientes):
            print(f"{i+1}: {cliente}")
    else:
        print("\nNão ha cliente para imprimir!")

while(loop):
    print("\n=========================================== Lista de clientes ===========================================")
    op = str(input("""
    O que você deseja fazer? Digite apenas o número da opção desejada.

    1 - Cadastrar
    2 - Deletar
    3 - Atualizar
    4 - Listar
    5 - Sair
    
    """))
    match op:
        case "1":
            nome = input("\nDigite o nome do cliente que deseja cadastrar: ")
            clientes.append(nome)
            mostrarClientes()

        case "2":
            mostrarClientes()
            delete = input("\nDigite o nome que deseja deletar: ")
            try:
                clientes.remove(delete)
                mostrarClientes()
            except:
                print("\nNome invalido!!!")
                
                
        case "3":
            mostrarClientes()
            atualizar = int(input("\nDigite o numero do nome que deseja atualizar: "))
            if atualizar-1 >= 0 and atualizar-1 < len(clientes):
                clientes[atualizar-1] = input("\nDigite o novo nome: ")
                mostrarClientes()
            else:
                print("\nValor invalido!!")
                
                
        case "4":
            mostrarClientes()
            

        case "5":
            loop = False
            
        case _:
            print("Opção invalida!!")