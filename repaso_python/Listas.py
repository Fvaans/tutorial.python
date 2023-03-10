# Lista
print("Crear listas de números, letras, mixta")
numeros = [1, 2, 3, 4, 5]
letras = ["a", "b", "c", "d"]
mezclado = [1, "a", True, 3.14, ["x", "y", "z"]]

print(numeros, letras, mezclado)


# Listas enlazadas
print("Lista enlazada")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

my_list = LinkedList()

my_list.add(1)
my_list.add(2)
my_list.add(3)

my_list.print_list()

#Operaciones con listas

print("Operaciones con listas")

#Acceder a un elemento
print("Acceder a un elemento")
my_list = [1, 2, 3, 4, 5]
print(my_list[0])
print(my_list[2])

#Agregar un elemento
print("Agregar un elemento")
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

my_list.extend([5, 6, 7])
print(my_list)

#Eliminar elementos
print("Eliminar elementos")
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)
print(my_list)

my_list.pop(2)
print(my_list)

#Ordenar elementos
print("Ordenar elementos")
my_list = [4, 1, 5, 9, 2, 6, 3]
my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)

#Buscar elementos
print("Buscar un elemento")
my_list = [1, 2, 3, 4, 5]
print(my_list.index(4))

#Extender listas
print("Extender una lista")
x = [1, 2]
x.extend([3, 4])
print(x)
Output: [1, 2, 3, 4]

