from BasicFunctions.funcoesBasicas import limpar

limpar()
#======================================================================


def somar(a,b):
    return a + b

print(somar(2,5))
# a funcao acima é a mesma coisa que o codigo abaixo

soma = lambda a,b: a + b
print(soma(2,5))


#======================================================================

#diferença de dois numeros
subtracao = lambda a,b: a-b
print(subtracao(10,7))

#produto de dois numeros
produto = lambda a,b: a*b
print(produto(10,4))

#quadrado de um numeros
quadrado = lambda a: a**2
print(quadrado(7))

#======================================================================

numeros = [-15,-5,-4,-3,-2,-1,0,1,2,3,4,5,15]

#======================================================================

dobro = list(map(lambda x: x*2, numeros))

print(f"Dobro: {dobro}")


#======================================================================


#Gere uma nova lista contendo os sucessores de cada um dos numeros da lista 'numeros'
sucessores = list(map(lambda x: x+1, numeros))
print(f"Sucessores: {sucessores}")

#Gere uma nova lista contendo os antecessores de cada um dos numeros da lista 'numeros'
antecessores = list(map(lambda x: x-1, numeros))
print(f"Antecessores: {antecessores}")

#Gere uma nova lista contendo os sucessor do quintuplo de cada um dos numeros da lista 'numeros'
suc_quintuplo = list(map(lambda x: (x*5)+1, numeros))
print(f"Sucessores do quintuplo: {suc_quintuplo}")

#======================================================================

pares = list(filter(lambda x: x%2==0, numeros))
print(f"Pares: {pares}")

positivos = list(filter(lambda x: x>=0, numeros))
print(f"Positivos: {positivos}")

#======================================================================

#Faça o filtro dos numero impares
impares = list(filter(lambda x: x%2 >=1, numeros))
print(f"Impares: {impares}")

#Faça o filtro dos numeros negativos
negativos = list(filter(lambda x: x<0, numeros))
print(f"Negativos: {negativos}")

#Desafio
#faça o filtro dos numeros mulpilos de 3 e 5 ao mesmo tempo
multiplos_de_3_e_5 = list(filter(lambda x: x%3 == 0 and x%5 == 0 and x != 0, numeros))
print(f"Multiplos de 3 e 5 ao mesmo tempo: {multiplos_de_3_e_5}")
