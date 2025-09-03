# Desafio
# fazer o fatorial de um número
# passo 1 --> receber um NUMERO através do input
# passo2 ---> fazer um contador deste número ate 1 
# passo3 ---> multiplicar os valores em uma variável()

x = int(input("Digite um numero: "))

y = x

## Fatorial com While
while y > 1:
    y -= 1
    print(f"\n{x}*{y}={x*y}")
    x *= y

## Fatorial com for()
for i in range(x-1, 0, -1):
    print(f"\n{y}*{i}={y*i}")
    y *= i
