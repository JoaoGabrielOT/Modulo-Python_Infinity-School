from funcoesBasicas import *

limpar()
        


class Livro:
    def __init__(self,titulo,anoPubli,autor):
        self.titulo = titulo
        self.anoPubli = anoPubli
        self.autor = autor
        self.emprestado = False
        
        
class Membro:
    def __init__(self,numero_membro,nome,ano_nasc):
        self.numero_membro = numero_membro
        self.nome = nome
        self.ano_nasc = ano_nasc
        self.historico_livros_emprestados = []


class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.membros = []
    
    def adicionar_livro_catalogo(self,livro:Livro):
        if livro not in self.catalogo:
            self.catalogo.append(livro)
            print(textoCor("Livro adicionado ao catalogo!", Cores.VERDE))
        else:
            print(textoCor("Livro ja esta no catalogo!", Cores.VERMELHO))
    
    def cadastrar_membro(self,membro:Membro):
        if membro not in self.membros:
            print(textoCor("Membro cadastrado!", Cores.VERDE))
            self.membros.append(membro)
        else:
            print(textoCor("Membro ja esta cadastrado!", Cores.VERMELHO))
    
    def emprestar_livro(self,livro:Livro,membro:Membro):
        if livro not in self.catalogo:
            print(textoCor("Livro não disponivel no catalgo!", Cores.VERMELHO))
            return
        
        if membro not in self.membros:
            print(textoCor("Membro não cadastrado!", Cores.VERMELHO))
            return
        
        if livro.emprestado:
            print(textoCor("Livro ja foi emprestado!", Cores.VERMELHO))
            return
        else:
            livro.emprestado = True
            membro.historico_livros_emprestados.append(livro)
            print(textoCor(f"Livro '{livro.titulo}' foi emprestado para o Membro '{membro.nome}'", Cores.VERDE))
        
    def devolver_livro(self,livro:Livro):
        if livro not in self.catalogo:
            print(textoCor("Livro não esta no catalogo", Cores.VERMELHO))
            return

        if livro.emprestado:
            livro.emprestado = False
            print(textoCor(f"Livro devolvido!", Cores.VERDE))
        else:
            print(textoCor("Livro ja esta disponivel!", Cores.VERMELHO))
        
    def listar_livros_disponiveis(self):
        for livro in self.catalogo:
            if not livro.emprestado:
                print("="*50)
                print(textoCor(f"""
{livro.titulo}
{livro.anoPubli}
{livro.autor}
                """, Cores.AZUL))
                print("="*50)


l1 = Livro("Morte e vida severina", 1987, "Joao cabral de melo neli")
l2 = Livro("A Divina Comedia", 1308, "Dante Alighieri")
m1 = Membro(123456, "Joao Gabriel", 2003)
m2 = Membro(78946, "Maria Paula", 2003)
b1 = Biblioteca()

b1.adicionar_livro_catalogo(l1)
b1.adicionar_livro_catalogo(l1)

print()

b1.cadastrar_membro(m1)
b1.cadastrar_membro(m1)

print()

b1.emprestar_livro(l1, m1)
b1.emprestar_livro(l2, m1)
b1.emprestar_livro(l1, m2)
b1.cadastrar_membro(m2)
b1.emprestar_livro(l1, m2)
b1.devolver_livro(l1)
b1.emprestar_livro(l1, m2)
b1.devolver_livro(l2)
b1.adicionar_livro_catalogo(l2)
b1.devolver_livro(l2)
b1.listar_livros_disponiveis()
b1.devolver_livro(l1)
b1.listar_livros_disponiveis()
