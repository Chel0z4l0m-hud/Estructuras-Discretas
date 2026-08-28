# --- Ejercicio 1.1 ---
a = 'Carlo Jose Luis'
n = len(a)
print("--- 1.1 ---")
print(a[0], a[1], a[4], a[10], a[-1])
print(a[0], a[n-1])
print(a[-1], a[-n])
# print(a[n])      # Genera  IndexError
# print(a[1.5])    # Genera TypeError

# --- Ejercicio 1.2 ---
a2 = 'Juan Armando y Luren Amelia'
print("\n--- 1.2 ---")
print(a2[0:4], a2[1:5], a2[6:6], a2[3:], a2[:5], a2[:])
print(a2[-1:4], a2[4:-1])
print(a2 == a2[:7] + a2[7:])
print(a2[2:99], a2[99:2], a2[-99:2], a2[-99:99])
print(a2[15:20]) # Luren
print(a2[0:10:2], a2[:10:2], a2[-10::2], a2[::2], a2[::-1])

# --- Ejercicio 1.3 ---
print("\n--- 1.3 ---")
a = 456, 'mi papa', 789
print(type(a), len(a), a[1])
# print(a[20]) # Descomentar para ver IndexError
a_uno = (6)
print(type(a_uno))
a_uno_tupla = (6,)
print(type(a_uno_tupla))
vacia = ()
print(type(vacia), len(vacia))
a, b = 3, 'tu papa'
print(a, b)

# --- Ejercicio 1.4 ---
print("\n--- 1.4 ---")
a, b = 1, 2
a, b = b, a
print(a, b)
a, b = 5, 7
a, b = a-b, a+b
print(b, a)

# --- Ejercicio 1.5 ---
print("\n--- 1.5 ---")
print(divmod(10, 3))
print(divmod(-10, 3))

# --- Ejercicio 1.6 ---
print("\n--- 1.6 ---")
a = [456, 'mi papa', 789]
print(type(a), len(a), a[1], a[1][1])
a1 = []; a2 = [4]; a3 = [6,]
print(len(a1), len(a2), len(a3))
print(type((7)), type((7,)), type([7]), type([7,]))
x = [6, 5]; y = 5, 6
print(type(x), type(y))
c, d = [5, 7]
print(c, d)
c, d = d, c
print(c, d)

# --- Ejercicio 1.7 ---
print("\n--- 1.7 ---")
a = [4, 2, 13]
print(a)
a[0] = 5
print(a)
c = a
print(c)
a[0] = 4
print(a, c)
a = [7, 28, 9]
print(a, c)
# a = 11, 12, 13
# a[0] = 5 # Descomentar para ver TypeError

# --- Ejercicio 1.8 ---
print("\n--- 1.8 ---")
lista = [1, 2, 3]
lista[0] = 99
print(lista)
lista.append(4)
print(lista)
lista.pop(0)
print(lista)

# --- Ejercicio 1.9 ---
print("\n--- 1.9 ---")
b = ['p', 'r', 'o', 'c', 'e', 'd', 'i', 'm', 'i', 'e', 'n', 't', 'o']
print(len(b), b[3])
b.append('c'); print(b, len(b))
b.pop(); print(b, len(b))
b.pop(0); print(b, len(b))
b.insert(4, 'w'); print(b, len(b))
b.insert(-1, 'h'); print(b, len(b))
b.reverse(); print(b, len(b))

# --- Ejercicio 1.10 ---
print("\n--- 1.10 ---")
lista = [1, 2, 3]
lista[-1:] = [lista[-1], 4]
print(lista)
lista2 = [1, 2, 3]
lista2[1:2] = [99, lista2[1]]
print(lista2)
lista3 = [1, 2, 3]
lista3[1:2] = []
print(lista3)

# --- Ejercicio 1.11 ---
print("\n--- 1.11 ---")
a = [14, 15]
print(a.reverse(), a) # reverse retorna None y modifica la lista
b = [14, 15]
c = b[::-1]
print(b, c) # b no cambia, c es la nueva lista

# --- Ejercicio 1.12 ---
print("\n--- 1.12 ---")
def f(a):
    a[0] = a[0] + 1
    return a
a = [1, 2, 3]
b = f(a)
print("b =", b)
print("a =", a)

# --- Ejercicio 1.13 ---
print("\n--- 1.13 ---")
a = [1, 2, 3]
b = a[:]
c = a
b[0] = 99
print("a =", a, "b =", b, "c =", c)

def f_copia(a):
    copia = a[:]
    copia[0] = copia[0] + 1
    return copia
a = [1, 2, 3]
b = f_copia(a)
print("b =", b, "a =", a)

# --- Ejercicio 1.14 ---
print("\n--- 1.14 ---")
a = [1, 2, [3, 4]]
b = a[:]
b[0] = 99
b[2][0] = 88
print("a =", a, "b =", b)
a2 = [1, 2, (3, 4)]
b2 = a2[:]
b2[0] = 99
print("a2 =", a2, "b2 =", b2)

# --- Ejercicio 1.15 ---
print("\n--- 1.15 ---")
print(range(16))
print(type(range(16)))
print(list(range(16)), len(range(16)))
print(list(range(0, 16)), list(range(16, 16)))
print(list(range(13, 6, -2)), len(range(13, 6, -2)))
print(list(range(17)), range(17)[3])
print(range(17)[1:15:2], list(range(17)[1:15:2]))
print(len(range(17)), len(range(17)[1:15:2]))

# --- Ejercicio 1.16 ---
print("\n--- 1.16 ---")
print('a' in 'mi papa', 'b' in 'mi programa')
print('' in 'mi programa', '' in '')
print('a' in '', ' ' in '')
print(1 in [1, 2, 3, 5, 6], 1 in [[1, 2, 3], 3], 1 in range(5))

# --- Ejercicio 1.17 ---
print("\n--- 1.17 ---")
print([11, 12] + [13, 14])
print((11, 12) + (13, 14))
# print([11, 12] + (13, 14)) # Descomentar para ver TypeError

# --- Ejercicio 1.18 ---
print("\n--- 1.18 ---")
for x in [11, 11.2, 'tu mama', True]:
    if isinstance(x, (int, float)):
        print(f"{x} es número")
    else:
        print(f"{x} no es número")

def es_secuencia(obj):
    return isinstance(obj, (str, tuple, list, range))
print(es_secuencia([1, 2]), es_secuencia((1, 2)), es_secuencia("hola"))
print(es_secuencia(range(5)), es_secuencia(123), es_secuencia({1: 2}))

# --- Ejercicio 1.19 ---
print("\n--- 1.19 ---")
b = [1, 2, 3]
print(type(b), str(b), tuple(b), list(b))
c = (1, 2, 3)
print(tuple(list(c)) == c)
b = [1, 2, 3]
print(list(tuple(b)) == b)
c = 'Ana Paula'
print(str(c), tuple(c), list(c))
print(str(list(c)) == c)