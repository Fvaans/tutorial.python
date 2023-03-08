#Estructuras selectivas
print("EJEMPLO IF")

edad1 = 18

if edad1 >= 18:
  print("Eres mayor de edad")
  print(edad1)

print("EJEMPLO DE IF Y ELSE")

edad2 = 14

if edad2 >= 18:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad")
print(edad2)

#Caso especial
print("EJEMPLO CASO ESPECIAL")
edad3 = 25

if edad3 < 18:
  print("Eres menor de edad")
elif edad3 < 30:
  print("Eres joven")
elif edad3 < 60:
  print("Eres adulto")
else:
  print("Eres mayor de edad")

print(edad3)

#Estructuras repetitivas

print("EJEMPLO REPETITIVOS")
print("Ejemplo WHILE")

i = 1
while i <= 5:
  print(i)
  i += 1

print("Ejemplo FOR")

for i in range(1, 8):
  print(i)


