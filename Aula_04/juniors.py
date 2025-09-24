import os
os.system("clear")
# - Crie uma função contar_vogais que receba uma string e conte quantas vogais (a, e, i, o, u) existem nela.

def contarVogais(texto:str):
    texto = texto.lower()
    contagem = 0
    vogais = ('a', 'e', 'i', 'o', 'u')
    for letra in texto:
        if letra in vogais:
            contagem += 1
    return contagem

nome = "Joao"
vogais = contarVogais(nome)

print(f"Há {vogais} vogais em {nome}")

# - Crie uma função chamada contagem_regressiva que recebe um número n e imprime os números de n até 1, em contagem regressiva.

def contagemRegressiva(n:int):
    if n <= 0:
        print("O numero deve ser maior que 0")
    else:
        while n >= 1:
            print(n)
            n -= 1

contagemRegressiva(vogais)

# - Crie uma função calcular_imc que receba o peso e altura de uma pessoa e calcule o Índice de Massa Corporal (IMC), com valores padrões de peso 70 kg e altura 1.75 m.

def calcularIMC(peso:int = 70, altura:float =1.75):
    imc = peso/(altura*altura)
    return imc

peso = 120
altura = 1.85

print(f"O IMC de uma pessoa com peso {peso} e altura {altura} é {calcularIMC(peso, altura)}")

# - Crie uma função chamada media que receba três notas de um aluno e calcule e retorne a média delas.

def media(n1:float, n2:float, n3:float):
    media = n1+n2+n3/3
    return media

print(f"Média: {media(10, 7, 3)}")
# - Crie uma função par_ou_impar que receba um número e retorne uma string informando se o número é "par" ou "ímpar".

def parImpar(n):
    if n % 2 == 0:
        saida = "Par"
    else:
        saida = "Impar"

    return saida

print(f"O numero {vogais} é {parImpar(vogais)}")