#reto 1 - NIVEL INTERMEDIO/AVANZADO
#def retoav1():
import pprint
from datetime import datetime
discos = [ 
  { 
    "Nombre" : "A por ellos que son locos y cobardes",
    "Artista" : "Loquillo",
    "Año" : 1989,
    "Precio" : 30.0,
    "Genero" : "Rock"
  },
  {
    "Nombre" : "Clasicos",
    "Artista" : "Porretas",
    "Año" : 2000,
    "Precio" : 20.0,
    "Genero" : "Rock"
  },
  {
    "Nombre" : "Apocalypse Cow ",
    "Artista" : "Milk Inc",
    "Año" : 1998,
    "Precio" : 15.0,
    "Genero" : "Electro"
  },
  {
    "Nombre" : "Pump Up The Jam",
    "Artista" : "Technotronic",
    "Año" : 1993,
    "Precio" : 38.0,
    "Genero" : "Electro"
  },
  {
    "Nombre" : "In The Nightside Eclipse",
    "Artista" : "Emperor",
    "Año" : 1994,
    "Precio" : 55.0,
    "Genero" : "Black metal"
  },
  {
    "Nombre" : "Passage",
    "Artista" : "Samael",
    "Año" : 1996,
    "Precio" : 62.0,
    "Genero" : "Black metal"
  },
  {
    "Nombre" : "Icon",
    "Artista" : "Benighted",
    "Año" : 2008,
    "Precio" : 38.0,
    "Genero" : "Death metal"
  },
  {
    "Nombre" : "Thriller",
    "Artista" : "Michael Jackson",
    "Año" : 1982,
    "Precio" : 230.0,
    "Genero" : "Pop"
  },
  {
    "Nombre" : "Van Halen",
    "Artista" : "Van Halen",
    "Año" : 1978,
    "Precio" : 160.0,
    "Genero" : "Metal"
  },
  {
    "Nombre" : "The last Don",
    "Artista" : "Don Omar",
    "Año" : 2003,
    "Precio" : 5.0,
    "Genero" : "Reggaeton"
  }
  ]
#check 1: comprobamos que la lista se imprime correctamente
# print(len(discos[0]['Nombre']))
#pprint.pprint(discos)

#bucle para imprimir las lista de discos 
for idx, disc in enumerate(discos):
    print(f'> Nº disco: {idx+1} > Disco: {disc["Nombre"]} > Artista: {disc["Artista"]} > Precio: {disc["Precio"]} > Genero: {disc["Genero"]}')

carrito = list()
count = 0

while True:
    seleccion = int(input ("> Selecciona un disco y 0 para finalizar la compra: "))-1
    if seleccion == -1:
        break
    else:
        #opcion 1
        carrito.append(discos[seleccion])
        #otra 2
        #carrito.append({'album:'discos[seleccion]['Nombre']}, 'precio:' discos[seleccion]['Precio'], 'Genero:' discos[seleccion]['Genero'])

print (carrito)
count += 1

#check 2
#print(seleccion)
#print(discos[seleccion])

precioCarrito = 0
cantidadDescuento = 0

#opcion 1
for i in carrito:
    if i['Genero'] == 'Electro' or i['Genero'] == 'Black metal':
        precioCarrito += i['Precio']*0.7
        cantidadDescuento += i['Precio']*0.3
    else:
        precioCarrito += i['Precio']


'''
#opcion 2
for i in range(len(carrito)):
    if carrito[i]['Genero'] == 'Electro' or carrito[i]['Genero'] == 'Black metal':
        precioCarrito:float = i['Precio']*0.7
        cantidadDescuento:float = i['Precio']*0.3
    else:
        precioCesta = carrito[i]['Precio']
'''

'''
#opcion 3
for idx, i in enumerate(carrito):
    if carrito[idx]['genero'] == 'Electro' or carrito[idx]['genero'] == 'Black metal':
        precioCarrito:float = carrito[i]['Precio']*0.7
        cantidadDescuento:float = carrito[i]['Precio']*0.3
    else:
        precioCesta = carrito[i]['Precio']
'''

print(f'> Fecha: {datetime.now()}')
print(f'> Precio de la cesta: {precioCarrito}€')
print(f'> Precio del descuento: {cantidadDescuento}€')