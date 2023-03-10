# Tuplas
# Tuplas anidadas
print("Tupla anidada")
my_tuple = (1, 2, (3, 4), (5, 6, 7))
print("Acceder a la tupla en la posición: 2,1")
print(my_tuple[2][1])
print("Recorrido de la tupla anidada:")
for element in my_tuple:
    if isinstance(element, tuple):
        for subelement in element:
            print(subelement)
    else:
        print(element)

#Operaciones con Tuplas
print("Operaciones con Tuplas")
#Indexación
print("Indexación de una tupla")
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[3])

#Concatenación
print("Concatenar una tupla")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)

#Repetición
print("Repeticion de una tupla")
my_tuple = (1, 2, 3)
new_tuple = my_tuple * 3
print(new_tuple)

#Longitud
print("Obtencion de la longitud de la tupla")
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(len(my_tuple))

#Comparación
print("Comparar tuplas")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = (1, 2, 3)
print(tuple1 < tuple2)
print(tuple1 == tuple3)
print(tuple1 <= tuple2)
print(tuple1 >= tuple3)

#Desempaquetado
print("Desempaquetar una tupla")
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)
print(b)
print(c)