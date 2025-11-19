from datetime import datetime
from funcoesBasicas import *

limpar()


class Conta:
    def __init__(self,numero_conta,titular):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = 0.0
        self.data_criacao = datetime.now().date()

class ContaCorrente(Conta):
    def __init__(self, numero_conta, titular, cheque_especial, credito):
        super().__init__(numero_conta, titular)
        self.cheque_especial = cheque_especial
        self.credito = credito

class ContaPoupanca(Conta):
    def __init__(self, numero_conta, titular):
        super().__init__(numero_conta, titular)
        self.rendimento = 6
    
    def saque(self, valorASacar):
        if(self.saldo - valorASacar >= 0):
            self.saldo -= valorASacar
            return "Saque bem sucedido"
        else:
            return "Saldo insuficiente"
    
    def depositar(self, valorADepositar):
        self.saldo += valorADepositar
        return "Deposito bem sucedido"

    def tranferir(self, conta_destinada:Conta, valor):
        if(self.saldo - valor >= 0):
            self.saldo -= valor
            conta_destinada.saldo += valor
            print("Transferencia bem sucedida")
        else:
            print("Saldo insuficiente")


class Editora:
    def __init__(self,nome,email):
        self.nome = nome
        self.email = email

class Livro:
    def __init__(self,titulo,anoPub,editora:Editora):
        self.titulo = titulo
        self.anoPub = anoPub
        self.editora = editora

editora1 = Editora("Editora Teste", "teste@gmail.com")
livro1 = Livro("Livro Teste", 2025, editora1)

print()