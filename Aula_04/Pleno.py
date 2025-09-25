# imports
import os
import platform


#limpa a tela a cada rodagem
def limpar():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system("clear")


limpar()

# - Crie uma função chamada calculadora que receba três parâmetros: dois números e uma operação (como uma string: "soma", "subtração", "multiplicação", "divisão"). A função deve retornar o resultado da operação escolhida entre os dois números.

opcoes = ("soma", "subtração", "multiplicação", "divisão")


def calculadora(n1: int, n2: int, op: str):

    match op.lower():
        case "soma":
            saida = n1 + n2
        case "subtração":
            saida = n1 - n2
        case "multiplicação":
            saida = n1 * n2
        case "divisão":
            saida = n1 / n2
        case _:
            saida = f"Operação invalida. Escolha entre as opções: {opcoes}"

    return saida


for op in opcoes:
    print(calculadora(20, 5, op))

# - Crie uma função maior_numero que receba uma lista de números e retorne o maior número dessa lista.


def maior_numero(lista):
    saida = lista[0]
    for n in lista:
        if saida < n:
            saida = n
    return saida


print(maior_numero([12, 45, 7, 89, 23, 56, 3, 78]))

# - Crie uma função eh_palindromo que recebe uma string e retorna True se ela for um palíndromo (ou seja, se pode ser lida da mesma forma de trás para frente EXEMPLO NATAN), e False caso contrário.


def eh_palindromo(palavra: str):
    palavra = palavra.lower()
    reverso = palavra[::-1]
    if reverso == palavra:
        return True
    else:
        return False


print(eh_palindromo("Renner"))

# - Crie uma função desconto que receba o preço de um produto e um percentual de desconto (opcional, com valor padrão de 10%). A função deve retornar o preço com o desconto aplicado.


def desconto(preco: float, desconto: int = 10):
    saida = (preco / 100) * (100 - desconto)
    return saida


print(desconto(28.75, 45))
