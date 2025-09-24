marte = ("Marte", "3.396km", "Fina e rarefeita")

alunos_e_notas = [("João", 10.0), ("Maria", 9.0), ("Vitoria", 8.0)]
for aluno in alunos_e_notas:
    print(aluno)

# ======================================================================
from time import sleep
import os

clientes = []
loop = True
def mostrarClientes():
    if clientes:
        print("\nLista atual:")
        for i, cliente in enumerate(clientes):
            print(f"""
{i+1}: Nome: {cliente["nome"]}
   Numero: {cliente["numero"]}
   Email: {cliente["email"]}
            """)
    else:
        print("\nNão ha cliente para imprimir!")

os.system("clear")
while(loop):
    iguais = ("="*43)
    print(f"\n{iguais} Lista de clientes {iguais}")
    op = str(input("""
    O que você deseja fazer? Digite apenas o número da opção desejada.

    1 - Cadastrar
    2 - Deletar
    3 - Atualizar
    4 - Listar
    5 - Sair
    
    """))
    sleep(0.5)
    match op:
        case "1":
            os.system("clear")
            cliente = {}
            cliente["nome"] = input("\nDigite o nome do cliente que deseja cadastrar: ")
            cliente["numero"] = input("\nDigite o numero do cliente: ")
            cliente["email"] = input("\nDigite o email do cliente: ")
            clientes.append(cliente)
            mostrarClientes()
            sleep(0.5)

        case "2":
            mostrarClientes()
            delete = input("\nDigite o nome que deseja deletar: ")
            try:
                cliente.remove(delete)
                mostrarClientes()
            except:
                print("\nNome invalido!!!")
            sleep(0.5)
                
                
        case "3":
            os.system("clear")
            mostrarClientes()
            atualizar = int(input("\nDigite o numero do nome que deseja atualizar: "))
            if atualizar-1 >= 0 and atualizar-1 < len(cliente):
                cliente[atualizar-1] = input("\nDigite o novo nome: ")
                mostrarClientes()
            else:
                print("\nValor invalido!!")
            sleep(0.5)
                
                
        case "4":
            os.system("clear")
            mostrarClientes()
            sleep(0.5)
            

        case "5":
            os.system("clear")
            loop = False
            
        case _:
            os.system("clear")
            print("Opção invalida!!")
            sleep(0.5)