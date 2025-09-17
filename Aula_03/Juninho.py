filmes_favoritos = []

filmes_favoritos.append("Donnie Darko")
filmes_favoritos.append("Fight Club")
filmes_favoritos.append("Se7en")

filmes_favoritos.pop(1)
print(filmes_favoritos[0])
print(filmes_favoritos[-1])
print()
print()


# ==============================================================

playlist = ["The smiths", "The cure", "tears for fears"]

for musica in playlist:
    print(musica)
print()
print()


# ==================================================================

notas = [7,8,9,10]
media = 0

for nota in notas:
    media += nota
media /= notas.__len__()

print(f"Media: {media}")
