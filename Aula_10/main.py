from funcoesBasicas import *

limpar()

class Pessoa:
    def __init__(self,nome:str,altura:float,idade:int,peso:float):
        self.nome = nome
        self.altura = altura
        self.idade = idade
        self.peso = peso

    def __str__(self):
        return f"""{textoCor("Nome:", Cores.VERDE_CLARO)} {textoCor(self.nome, Cores.AZUL_CLARO)}
{textoCor("Altura:", Cores.VERDE_CLARO)} {textoCor(self.altura, Cores.AZUL_CLARO)}
{textoCor("Idade:", Cores.VERDE_CLARO)} {textoCor(self.idade, Cores.AZUL_CLARO)}
{textoCor("Peso:", Cores.VERDE_CLARO)} {textoCor(self.peso, Cores.AZUL_CLARO)}
            """

p1 = Pessoa(nome="João",altura=1.85, idade=22, peso=120.0)

#print(vars(p1))
print(p1)

# Façam uma class para representar um cachorro com, nome , cor e raça

class Cachorro:
    def __init__(self,nome:str,cor:str,raca:str):
        self.nome = nome
        self.cor = cor
        self.raca = raca
        self.patas = 4

    def setPatas(self, numeroPatas:int):
        self.patas = numeroPatas

    def __str__(self):
        return f"""{textoCor("Nome:", Cores.VERDE_CLARO)} {textoCor(self.nome, Cores.AZUL_CLARO)}
{textoCor("Cor:", Cores.VERDE_CLARO)} {textoCor(self.cor, Cores.AZUL_CLARO)}
{textoCor("Raça:", Cores.VERDE_CLARO)} {textoCor(self.raca, Cores.AZUL_CLARO)}
{textoCor("Patas:", Cores.VERDE_CLARO)} {textoCor(self.patas, Cores.AZUL_CLARO)}
            """
    
    def latir(self):
        return "RUUUFS"


c1 = Cachorro(nome="Pitoco", cor="Caramelo", raca="Vira-Lata")
c1.setPatas(3)
#print(vars(c1))
print(c1)
# print(c1.latir())

class Carro:
    def __init__(self,modelo:str,ano:int,cor:str):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0.0

    def acelerar(self,quantidade:int = 1):
        self.velocidade += 8*quantidade
        return self.velocidade

    def frear(self,quantidade:int = 1):
        self.velocidade -= 3*quantidade
        return self.velocidade

    def __str__(self):
        return f"""{textoCor("Cor:", Cores.VERDE_CLARO)} {textoCor(self.cor, Cores.AZUL_CLARO)}
{textoCor("Modelo:", Cores.VERDE_CLARO)} {textoCor(self.modelo, Cores.AZUL_CLARO)}
{textoCor("Ano:", Cores.VERDE_CLARO)} {textoCor(self.ano, Cores.AZUL_CLARO)}
{textoCor("Velocidade:", Cores.VERDE_CLARO)} {textoCor(self.velocidade, Cores.AZUL_CLARO)}
            """


carro1 = Carro(cor="Prata", modelo="Celta", ano=2003)

# print(vars(carro1))
carro1.acelerar(10)
carro1.frear(10)
print(carro1)


