#ejercicio 22, recursividad: el problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con ayuda de la fuerza” realizar las siguientes actividades:
# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más objetos en la mochila;
# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
# c. Utilizar un vector para representar la mochila.

def usar_la_fuerza(mochila, objetos_sacados=0):
    if len(mochila) > 0:
        if mochila[0] == "sable de luz":
            return True, objetos_sacados + 1
        else:
            return usar_la_fuerza(mochila[1:], objetos_sacados + 1)
    else:
        return False, objetos_sacados

# Ejemplo de uso

mochila = ["comida", "botiquín", "sable de luz", "agua"]
encontrado, cantidad = usar_la_fuerza(mochila)

if encontrado:
    print(f"¡Sable encontrado! Se sacaron {cantidad} objetos.")
else:
    print("No había sable de luz en la mochila.")