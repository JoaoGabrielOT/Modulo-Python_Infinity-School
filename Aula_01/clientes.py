def mostrarNomes():
    for i in clientes:
        print(f"{clientes.index(i)}: {i}")
    print()

clientes = ["João", "Maria", "Raphael C.", "Raphael A.", "Vitoria"]
mostrarNomes()

clientes.append("Novo nome")
mostrarNomes()

clientes.pop(0)
mostrarNomes()

clientes[1] = "Danilo"
mostrarNomes()

clientes.remove("Vitoria")
mostrarNomes()