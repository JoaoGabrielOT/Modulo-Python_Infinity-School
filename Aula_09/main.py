import flet as ft


def main(pagina:ft.Page):
    #implemente uma função para receber o nome e a senha da pessoa e cadastrar em uma lista
    clientes = []

    def clicar(e):
        clientes.append({
            "ID": len(clientes),
            "Nome": nome.value,
            "Senha": senha.value
            })
        
        nome.value = ""
        senha.value = ""

        print(clientes)
        # showClientes.text = clientes

        showClientes.controls.append(ft.Text(clientes[-1]))
        pagina.update()

    ola = ft.Text("Olá Mundo", size=50)
    nome = ft.TextField(hint_text="Digite o seu nome: ")
    senha = ft.TextField(hint_text="Digite a sua senha: ")
    botao = ft.ElevatedButton("Cadastrar", on_click=clicar)
    
    showClientes = ft.Column([])
    

    pagina.add(ola, nome, senha, botao, showClientes)
    pass


ft.app(target=main)