from random import randint
from funcoesBasicas import *

limpar()

menor = 1
maior = 10

numero = randint(menor, maior)

print(textoCor(f"Um numero aleatorio foi criado!!! ({menor}-{maior})\nTeste adivinha-lo!", Cores.CIANO))

while True:
    try:
        tentativa = int(input(f"{textoCor("Digite sua tentativa:", Cores.FUNDO_CIANO)} "))

        if tentativa < menor or tentativa > maior:
            limpar()
            print(textoCor(f"Valor invalido!! Deve ser no intervalo de {menor} a {maior}\n", Cores.VERMELHO))

        elif tentativa < numero:
            limpar()
            print(textoCor("O numero gerado é maior!!\n", Cores.AMARELO))

        elif tentativa > numero:
            limpar()
            print(textoCor("O numero gerado é menor!!\n", Cores.AMARELO))

        elif tentativa == numero:
            limpar()
            print(textoCor("Parabens!!! voce acertou!\n", Cores.VERDE))
            break
    
    except Exception as e:
        limpar()
        print(textoCor(f"Erro: {e}\n", Cores.VERMELHO))