# Definición de una función para ordenar una lista de números
def ordenar_lista(lista):
    try:
        # Intentamos ordenar la lista y devolverla
        lista_ordenada = sorted(lista)
        return lista_ordenada
    except TypeError:
        # Si ocurre una excepción de tipo (por ejemplo, si la lista contiene elementos que no son números),
        # se devuelve un mensaje de error.
        return "Error: La lista contiene elementos que no son números."

# Función de login para verificar las credenciales del usuario
def login():
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    
    if usuario == "joel" and contraseña == "chan":
        return True
    else:
        return False

# Función para procesar la entrada del usuario y obtener solo los números válidos
def procesar_entrada(entrada):
    numeros = []
    for elemento in entrada.split():
        try:
            numero = float(elemento)
            numeros.append(numero)
        except ValueError:
            # Si no se puede convertir a número, se ignora el elemento.
            continue
    return numeros

if __name__ == "__main__":
    # Verificación de login
    while not login():
        print("Acceso denegado. Introduce credenciales válidas.")
    
    # Ingresar lista de números
    numeros = []
    while len(numeros) < 6:
        entrada = input("Ingresa un número: ")
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Ignorando entrada no válida. Ingresa un número.")
    
    resultado = ordenar_lista(numeros)

    # Imprimir la lista ordenada con formato adecuado para números enteros
    resultado_formateado = [int(num) if num.is_integer() else num for num in resultado]
    print("Lista ordenada de menor a mayor:", resultado_formateado)
