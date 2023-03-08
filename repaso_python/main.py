# Tipos de datos primitivos
# Numeros enteros

numero1: int = 57
print(numero1)

numero2 = 24
print(numero2)

# Numeros reales

numero3: float = 4.9
print(numero3)

numero4 = 5.0
print(numero4)

# Booleanos

esColombiano: bool = True
esArgentino = False
print(esColombiano)

# Caracter y cadena de caracteres

mensaje = "Cadena con una comilla simple ', una comilla doble \" y una diagonal invertida \\"
print(mensaje)

# Operadores
# Aritmeticos

numero5 = 9
numero6 = 12
suma = numero6 + numero5
resta = numero6 - numero5
multiplacion = numero6 * numero5
division = numero6 / numero5
modulo = numero6 % numero5
print("La suma es =", suma)
print("La resta es=", resta)
print("La multiplacion es=", multiplacion)
print("La division es=", division)
print("El modulo es=", modulo)

# Asignación
x = 7
y = 8
z = 2
print(x)

# Logicos
# and(y)

q = 5
print(q > 4 and q < 9)

# or (o)
p = 4
print(p > 5 or p < 10)

# not
print(not (p > 2 and q < 7))

# Relacionales

valor1 = 7
valor2 = 9

print(valor1 == valor2)  # Igualdad
print(valor1 > valor2)  # Mayor que
print(valor1 < valor2)  # Menor que
print(valor1 >= valor2)  # Mayor igual que
print(valor1 <= valor2)  # Menor igual que
print(valor1 != valor2)  # Diferente

# Funciones
"""
 LAS FUNCIONES SON UN BLOQUE DE CODIGO QUE SOLO SE EJECUTAN CUANDO SE LLAMAN.
"""


def my_function():
    print("¡Feliz dia!")


my_function() # Invocar la funcion

def message(name, lastname):
    print("¡Feliz dia!" + name + " " +lastname)


message("Sara", "Burbano")

