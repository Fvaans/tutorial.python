#Diccionarios
#Crear
print("Crear un diccionario")
dic = {'nombre': 'Sara', 'edad': 20, 'ciudad': 'Barcelona'}
print(dic)
#Accediendo al diccionario
print("Accedemos al valor Sara por la clave nombre")
print(dic['nombre'])

#Agregar una nueva clave con valor
print("Agregamos una nueva clave y su valor")
dic['profesion'] = 'Docente'
print(dic)

#Modificar
print("Modificamos un valor")
dic = {'nombre': 'Sara', 'edad': 20, 'ciudad': 'Barcelona'}
dic ['edad'] = 21
print(dic)

#Eliminar
print("Eliminamos una clave")
del dic['edad']
print(dic)

#Recorrer
for valor in dic.values():
    print(valor)  
