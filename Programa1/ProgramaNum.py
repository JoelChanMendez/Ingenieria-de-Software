def ordenar_lista(lista):
    try:
        lista_ordenada = sorted(lista)
        return lista_ordenada
    except TypeError:
        return "Error: La lista contiene elementos que no son números."

if __name__ == "__main__":
    entrada = input("Ingresa una lista de números separados por espacios: ")
    numeros = entrada.split()
    try:
        numeros = [float(numero) for numero in numeros]
        resultado = ordenar_lista(numeros)
        print("Lista ordenada de menor a mayor:", resultado)
    except ValueError:
        print("Error: Ingresa números válidos separados por espacios.")
