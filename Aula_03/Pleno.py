nomes = ["Gabriel", "Juliano", "Anna", "Marcos"]

for nome in nomes:
    print(f"O nome {nome} possui {nome.lower().count("a")} letra(s) 'a'")
print()
print()

# =====================================================================

contador = 0
for nome in nomes:
    if nome.startswith("A"):
        contador += 1
print(f"{contador} nome(s) das lista começam com a letra 'A'")
print()
print()

# =====================================================================

numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    print(f"{numero}**2 = {numero**2}")