import flet as ft

def main(pagina:ft.Page):
    produtos = []
    showProdutos = ft.Column([])

    def adicionar(e):
        produtos.append({
            "ID": len(produtos),
            "Nome": nomeProduto.value,
            "Preco": precoProduto.value,
            "Quantidade": quantidadeProduto.value
        })
        nomeProduto.value = ""
        quantidadeProduto.value = ""
        precoProduto.value = ""

    def carregar(e):
        showProdutos.controls.clear()
        for produto in produtos:
            if produto not in showProdutos:
                showProdutos.controls.append(ft.Text(f"""
                Produto {produto["ID"]+1}:
                    Nome: {produto["Nome"]} | Preço: {produto["Preco"]} | Quantidade: {produto["Quantidade"]}"""))
        
        pagina.update()


    
    titulo = ft.Text("Gerenciador de estoque")

    nomeProduto = ft.TextField(hint_text="Insira o nome do produto.")
    precoProduto = ft.TextField(hint_text="Insira o preço do produto.")
    quantidadeProduto = ft.TextField(hint_text="Insira a quantidade do produto.")
    botaoAdicionar = ft.ElevatedButton("Adicionar produto", on_click=adicionar)
    botaoCarregar = ft.ElevatedButton("Carregar produtos", on_click=carregar)

    botoes = ft.Row([botaoAdicionar, botaoCarregar])

    pagina.add(titulo, nomeProduto, precoProduto, quantidadeProduto, botoes, showProdutos)


ft.app(target=main)