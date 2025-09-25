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

#  - Crie uma função chamada fatorial que calcule o fatorial de um número.


def fatorial(num: int):
    if num < 0:
        saida = "Parametro deve ser 0 ou numero positivo."
    elif num == 0:
        saida = 1
    else:
        saida = num
        while num != 1:
            num -= 1
            saida *= num
    return saida


print(fatorial(5))

# - Crie uma função que receba um numero inteiro como parâmetro e retorna a sequencia fibonnaci ate aquela ordem respectiva.


def fibonnaci(num):
    a = 1
    b = 1
    c = a + b
    sequencia = []
    sequencia.append(a)
    sequencia.append(b)
    sequencia.append(c)
    while a < num or b < num or c < num:
        a = b + c
        if a <= num:
            sequencia.append(a)

        b = c + a
        if b <= num:
            sequencia.append(b)

        c = a + b
        if c <= num:
            sequencia.append(c)

    return sequencia


print(fibonnaci(144))
