marte = ("Marte", "3.396km", "Fina e rarefeita")

alunos_e_notas = [("João", 10.0), ("Maria", 9.0), ("Vitoria", 8.0)]
for aluno in alunos_e_notas:
    print(aluno)

# ======================================================================
from time import sleep
import os

clientes = []
loop = True

def textoCor(texto, cor):
    saida = f"\033[{cor}m{texto}\033[0m"
    return saida

vermelho = 31
verde = 32
amarelo = 33
azul = 34
ciano = 36

def mostrarClientes():
    if clientes:
        print("\nLista atual:")
        for i, cliente in enumerate(clientes):
            print(f"""
{i+1}: {textoCor("Nome:", amarelo)} {textoCor({cliente["nome"]}, ciano)}
   {textoCor("Numero:", amarelo)} {textoCor({cliente["numero"]}, ciano)}
   {textoCor("Email:", amarelo)} {textoCor({cliente["email"]}, ciano)}
            """)
    else:
        print("\nNão ha cliente para imprimir!")

os.system("clear")

while(loop):
    iguais = ("="*43)
    print(f"\n{textoCor(f"{iguais} Lista de clientes {iguais}", ciano)}")
    op = str(input(f"""
    O que você deseja fazer? Digite apenas o número da opção desejada.

    {textoCor("1", amarelo)} - Cadastrar
    {textoCor("2", amarelo)} - Deletar
    {textoCor("3", amarelo)} - Atualizar
    {textoCor("4", amarelo)} - Listar
    {textoCor("5", amarelo)} - Sair
    
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
            delete = int(input("\nDigite o numero do cliente que deseja deletar: "))
            if delete-1 >= 0 and delete-1 < len(clientes):
                clientes.pop(delete)
                mostrarClientes()
            else:
                print(f"\n{textoCor("Valor invalido!!!", vermelho)}")
            sleep(0.5)
                
                
        case "3":
            os.system("clear")
            mostrarClientes()
            atualizar = int(input("\nDigite o numero do cliente que deseja atualizar: "))
            if atualizar-1 >= 0 and atualizar-1 < len(clientes):
                cliente = clientes[atualizar - 1]

                cliente["nome"] = input("\nDigite o novo nome: ")
                cliente["numero"] = input("\nDigite o novo numero: ")
                cliente["email"] = input("\nDigite o novo email: ")
                
                mostrarClientes()
            else:
                print(f"\n{textoCor("\nValor invalido!!", vermelho)}")
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
            print(f"\n{textoCor("Opção invalida!!!", vermelho)}")
            sleep(0.5)