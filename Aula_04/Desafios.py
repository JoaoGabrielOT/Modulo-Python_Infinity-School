# imports
import random
import os
import platform


#limpa a tela a cada rodagem
def limpar():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system("clear")


limpar()

# Faça um gerador de senhas aleatórias , que receba como parâmetros o tamanho da senha , que por padrão inicia em 6


def geradorSenhas(tamanho: int = 6):
    maximo = 10**tamanho - 1
    minimo = 10**(tamanho - 1)

    saida = random.randint(minimo, maximo)
    return saida


senha = geradorSenhas(4)

# Faça um descobridor de senhas de 4 digitos .(Enunciado é curto mais o problema é longo)Use a criatividade !


def descobrirSenha(senha):
    tamanhoDaSenha = len(str(senha))
    if tamanhoDaSenha == 4:
        crypto = 1000
        contagem = 0
        while crypto != senha:
            crypto += 1
            contagem += 1
        saida = f"A senha é {crypto}, precisei de {contagem} tentativas para descobrir."
    else:
        saida = "A senha deve ser de 4 digitos."

    return saida


print(descobrirSenha(senha))
