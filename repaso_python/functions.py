#Entradas
base = float(input("Ingresa la base: "))
altura = float(input("Ingresa la altura: "))

# Proceso
def calcularAreaTriangulo(b, al):
    area = (b * al) / 2
    return area

#Salida
resultado = calcularAreaTriangulo(base, altura)
print("El area del triangulo es: ", resultado)


# Función con argumentos por defecto
def mostrarPais(pais = "Colombia"):
    print("Yo soy de: " + pais)

mostrarPais("Suiza")
mostrarPais("Ecuador")
mostrarPais()
mostrarPais("Brasil")