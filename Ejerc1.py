# EJERCICIO 1
print("\n--- EJERCICIO 1: Lista de colores ---")
n = int(input("Mencionar cuántos colores tiene la lista: "))
if n <= 0:
    print("¡Imposible!")
else:
    colores = []
    for i in range(n):
        color = input(f"Mencionar el color {i+1}: ")
        colores.append(color)
    print(f"La lista de color es: {colores}")


# EJERCICIO 6
print("\n--- EJERCICIO 6: Invertir lista ---")
n = int(input("Mencionar cuántas palabras tiene la lista: "))
palabras = []
for i in range(n):
    palabras.append(input(f"Mencionar la palabra {i+1}: "))

print(f"La lista creada es: {palabras}")

# Con reverse()
copia1 = palabras[:]
copia1.reverse()
print(f"La lista inversa (con reverse) es: {copia1}")

# Con slice [::-1]
copia2 = palabras[::-1]
print(f"La lista inversa (con slice) es: {copia2}")


# EJERCICIO 11: Suma de listas
print("\n--- EJERCICIO 11: Suma de listas ---")
n = int(input("Ingrese la cantidad de elementos (n): "))
lista1 = []
lista2 = []

print("Ingrese los elementos de la Lista 1:")
for i in range(n):
    lista1.append(int(input(f"  Elemento {i+1}: ")))

print("Ingrese los elementos de la Lista 2:")
for i in range(n):
    lista2.append(int(input(f"  Elemento {i+1}: ")))

lista3 = [lista1[i] + lista2[i] for i in range(n)]

print(f"Lista1 = {lista1}")
print(f"Lista2 = {lista2}")
print(f"Lista3 = {lista3}")


# EJERCICIO 12: Producto escalar
print("\n--- EJERCICIO 12: Producto escalar ---")
v1 = [15, 12, 4]
v2 = [-11, 13, -1]

producto_escalar = sum(v1[i] * v2[i] for i in range(len(v1)))

print(f"Vector 1: {v1}")
print(f"Vector 2: {v2}")
print(f"Producto escalar: {producto_escalar}")

# EJERCICIO 13: Quitar vocales
print("\n--- EJERCICIO 13: Quitar vocales ---")
texto = input("Ingrese una cadena de texto: ")

# Agregamos las vocales con tilde por si acaso
vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
resultado = "".join([letra for letra in texto if letra not in vocales])

print(f"Texto original: {texto}")
print(f"Texto sin vocales: {resultado}")

print("\n" + "="*40)
print("¡Fin de los ejercicios prácticos!")
print("="*40)