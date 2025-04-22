#ejercicio 5, recursividad: Desarrollar una función que permita convertir un número romano en un número decimal.#

# Diccionario con los valores de los números romanos
valores = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def numRomano(romano):
    if len(romano) == 0:
        return 0
    if len(romano) == 1:
        return valores[romano]
        
    actual = valores[romano[0]]
    siguiente = valores[romano[1]]

    if actual < siguiente:
        # Si el valor actual es menor al siguiente, se resta
        return -actual + numRomano(romano[1:])
    else:
        # Si no, se suma
        return actual + numRomano(romano[1:])
    

#llamado#

romano = input("Ingresá un número romano (en mayúsculas): ")
print("Valor decimal:", numRomano(romano))