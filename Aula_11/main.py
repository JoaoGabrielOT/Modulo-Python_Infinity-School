from funcoesBasicas import *

limpar()

class Pessoa:

    def __init__(self,nome:str,idade:int,altura:float,peso:float):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.IMC = self.calcularIMC()
    

    def calcularIMC(self):
        return self.peso/(self.altura**2)
    

    def setAltura(self,altura):
        self.altura = altura
        self.IMC = self.calcularIMC()

    def getAltura(self):
        return self.altura


    def setPeso(self,peso):
        self.peso = peso
        self.IMC = self.calcularIMC()

    def getPeso(self):
        return self.peso


pessoa1 = Pessoa("João",22,1.85,90)

print(pessoa1.IMC)
pessoa1.setPeso(120)
print(pessoa1.IMC)
pessoa1.setAltura(1.95)
print(pessoa1.IMC)



class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

class Gato(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome, cor)

class Cachorro(Animal):
    def __init__(self, nome, cor, raca):
        super().__init__(nome, cor)
        self.raca = raca

gato1 = Gato("Mingau","Laranja")
cachorro1 = Cachorro("Pitoco", "Caramelo", "vira-lata")

print(f"""
{textoCor("Nome:", Cores.VERDE_CLARO)} {textoCor(gato1.nome, Cores.AZUL_CLARO)}
{textoCor("Cor:", Cores.VERDE_CLARO)} {textoCor(gato1.cor, Cores.AZUL_CLARO)}
""")

print(f"""
{textoCor("Nome:", Cores.VERDE_CLARO)} {textoCor(cachorro1.nome, Cores.AZUL_CLARO)}
{textoCor("Cor:", Cores.VERDE_CLARO)} {textoCor(cachorro1.cor, Cores.AZUL_CLARO)}
{textoCor("Raça:", Cores.VERDE_CLARO)} {textoCor(cachorro1.raca, Cores.AZUL_CLARO)}
""")


class VeiculoAutomotorTerrestre:
    def __init__(self,modelo,ano,cor,rodas):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.rodas = rodas

class Carro(VeiculoAutomotorTerrestre):
    def __init__(self, modelo, ano, cor, rodas):
        super().__init__(modelo, ano, cor, rodas)


class Moto(VeiculoAutomotorTerrestre):
    def __init__(self, modelo, ano, cor, rodas):
        super().__init__(modelo, ano, cor, rodas)



class Conta:
    def __init__(self,numero_conta,titular):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = 0.0

class ContaCorrente(Conta):
    def __init__(self, numero_conta, titular, cheque_especial, credito):
        super().__init__(numero_conta, titular)
        self.cheque_especial = cheque_especial
        self.credito = credito

class ContaPoupanca(Conta):
    def __init__(self, numero_conta, titular):
        super().__init__(numero_conta, titular)
        self.rendimento = 6