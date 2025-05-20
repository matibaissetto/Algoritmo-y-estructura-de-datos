#ejercicio 24, pila

print(f"INICIO EJERCICIO 24")

def lista_personajes(nombre, peliculas):
    return {
        "nombre" : nombre,
        "peliculas" : peliculas
    }

personajes_marvel = []
personajes_marvel.append(lista_personajes("Iron Man", 10))
personajes_marvel.append(lista_personajes("Capitan America", 9))
personajes_marvel.append(lista_personajes("Thor", 7))
personajes_marvel.append(lista_personajes("Black Widow", 6))
personajes_marvel.append(lista_personajes("Hulk", 7))
personajes_marvel.append(lista_personajes("Groot", 2))
personajes_marvel.append(lista_personajes("Spider Man", 7))
personajes_marvel.append(lista_personajes("Scarlet witch", 4))
personajes_marvel.append(lista_personajes("Rocket Raccon", 3))


print(personajes_marvel)

print(f"ITEM A")
for personaje in range(len(personajes_marvel) -1, -1, -1):
    if personajes_marvel[personaje]["nombre"] == "Rocket Raccon" or personajes_marvel[personaje]["nombre"] == "Groot":
        posicion = len(personajes_marvel) -personaje
        print(f"{personajes_marvel[personaje]["nombre"]} esta en la posicion:  {posicion}")
            
print("ITEM B")
for personaje in personajes_marvel:
    if personaje["peliculas"] > 5:
        print(f" la cantidad de peliculas en las que actuo {personaje["nombre"]} es de: {personaje["peliculas"]}")

print(f"ITEM C")
for personaje in personajes_marvel:
    if personaje["nombre"] == "Black Widow":
        print(f"las peliculas en las que participo {personaje["nombre"]} fueron: {personaje["peliculas"]}")

print(f"ITEM D")
for personaje in personajes_marvel:
    if personaje["nombre"].startswith(("C", "D", "G")):
        print(f"Los nombres de los personajes cuyos nombres empiezan con C, D o G son: {personaje["nombre"]}")