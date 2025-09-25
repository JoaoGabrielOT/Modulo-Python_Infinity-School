marte = ("Marte", "3.396km", "Fina e rarefeita")

alunos_e_notas = [("João", 10.0), ("Maria", 9.0), ("Vitoria", 8.0)]
for aluno in alunos_e_notas:
    print(aluno)

# ======================================================================
from time import sleep
import os
import json
import platform

try:
    with open('clientes.json', 'r') as arquivo:
        clientes = json.load(arquivo)
except FileNotFoundError:
    clientes = []
    

loop = True

vermelho = 31
verde = 32
amarelo = 33
azul = 34
ciano = 36

# funcao para definir a cor da escrita no terminal
def textoCor(texto:str, cor:int):
    saida = f"\033[{cor}m{texto}\033[0m"
    return saida


# funcao para mostrar clientes
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
        print("\nNão ha nenhum cliente cadastrado!")


# funcao para limpar o terminal
def limpar():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system("clear")


def pausa(time:float = 0.5):
    sleep(time)


# funcao para salvar os clientes no arquivo json
def salvarClientes():
    with open('clientes.json', 'w') as arquivo:
        json.dump(clientes, arquivo, indent=4)


limpar()
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
    pausa()
    match op:
        case "1":
            limpar()
            cliente = {}
            try:
                cliente["nome"] = input("\nDigite o nome do cliente que deseja cadastrar: ")
                cliente["numero"] = input("\nDigite o numero do cliente: ")
                cliente["email"] = input("\nDigite o email do cliente: ")
                clientes.append(cliente)
                salvarClientes()
                mostrarClientes()
            except Exception as e:
                limpar()
                print(f"{textoCor("erro:", vermelho)} {e}")
            pausa()

        case "2":
            limpar()
            mostrarClientes()
            if clientes:
                try:
                    delete = int(input("\nDigite o numero do cliente que deseja deletar: "))
                    if delete - 1 >= 0 and delete - 1 < len(clientes):
                        clientes.pop(delete - 1)
                        salvarClientes()
                        mostrarClientes()
                    else:
                        limpar()
                        print(f"\n{textoCor("Valor invalido!!!", vermelho)}")
                except Exception as e:
                    limpar()
                    print(f"{textoCor("erro:", vermelho)} {e}")
            pausa()
                
                
        case "3":
            limpar()
            mostrarClientes()
            if clientes:
                try:
                    atualizar = int(input("\nDigite o numero do cliente que deseja atualizar: "))
                    if atualizar-1 >= 0 and atualizar-1 < len(clientes):
                            cliente = {}

                            cliente["nome"] = input("\nDigite o novo nome: ")
                            cliente["numero"] = input("\nDigite o novo numero: ")
                            cliente["email"] = input("\nDigite o novo email: ")
                            
                            clientes[atualizar - 1] = cliente
                            salvarClientes()
                            mostrarClientes()
                    else:
                        print(f"\n{textoCor("\nValor invalido!!", vermelho)}")
                except Exception as e:
                    limpar()
                    print(f"{textoCor("erro:", vermelho)} {e}")
            pausa()
                
                
        case "4":
            limpar()
            mostrarClientes()
            pausa(2)
            

        case "5":
            limpar()
            loop = False
            
        case _:
            limpar()
            print(f"\n{textoCor("Opção invalida!!!", vermelho)}")
            pausa()