# Esto es un comentario
'''
Esto es comentario
largo
'''
print("Hola Mundo")
user = "Martin"
print("Hola" + "Martin")
print("Hola" + " " + "Martin")
print("Hola" + " " + user)
user = 200
user = user * 2
print (user)

newUser:str = "Pepe"
print(newUser)
newUser = 3
print(newUser)

user = "Juan"
#f formatea el valor en texto
print(f"Hola {newUser}!")
print(f"Hola {user}!")

bienvenida = f"Hola {user}"
print(f"Hola {newUser}!")
print(f"{bienvenida}, tu numero de usuario es {newUser}")
#con comillas triples podemos imprimir varias lineas
print(f'''{bienvenida}, 
tu numero de usuario es {newUser}''')

print(f'''{bienvenida}, 
     tu numero de usuario es {newUser}''')

print(f"""{bienvenida}, 
     tu numero de usuario es {newUser}""")

#tipos variables
'''
bool
str
int
float
list [ ..., ...]
tuple ( ..., ...)
dict { key: value, key: value,.. }
set
range
complex
frozenset
bytes
'''

#Declaracion BOOL
casado: bool = True
print(f'Casado? {casado}')

#Creacion LISTAS
miLista: [str] = ["Martin", "Juan", "Pablo"]
print(miLista)
#otra forma de imprimir con iteracion y mejor visualizacion
print(*miLista)
#imprimir la posicion 1 de la lista, en este caso Juan
print(miLista[1])


listaCompra: [str] = ["Tomates", "Patatas", "Huevos", "Jamon", "Vino"]
#forma extraer los 2 ultimos argumentos
print(*listaCompra[-2:])
#otra forma menos desarrollada
print(listaCompra[-2], listaCompra[-1])

#RANGOS
#extraemos los numeros del 0 al 10 solo pares
miRango= range(0,11,2)
print(*miRango)
#saber si un numero es par
esPar= 4%2
print(esPar)

#busqueda en bibliotecas
datos = {
  "name": "David", 
  "age":33, 
  "DNI":"29180380G"
     }
print(datos["DNI"])
print(f'El DNI de {datos["name"]} es {datos["DNI"]}.')

#sacar los numeros nos repetidos
misNumeros = [8,1,1,2,3,4,9,5,8,6,7,8,9,3,2,5,3]
lista = set(misNumeros)
print(*lista)

#otra forma de crear set
miOtroSetDeDatos = set(["a","a","a","b"])
print(*miOtroSetDeDatos)

#ordenar lista
listado = [2,4,7,8,9,23,45,61,6,8,0,8,4]
listado.sort()
print(listado)

#invertir lista
listado.reverse()
print(listado)

#para que el usuario introduzcas datos
name = input("Dime tu nombre: ")
print(f"Has escrito: {name}")
edad = int(input("Cual es tu edad?"))
print(f"Hola: {name} tienes {edad} años")