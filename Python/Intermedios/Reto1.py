#reto 1 - NIVEL INTERMEDIO/AVANZADO
#def retoav1():
import pprint
from datetime import datetime
discos = [ 
  {
  "Disco_num" : 1,
  "Nombre" : "A por ellos que son locos y cobardes",
  "Artista" : "Loquillo",
  "Año" : 1989,
  "Precio" : 30.0,
  "Genero" : "Rock"
  },
  {
  "Disco_num" : 2,
  "Nombre" : "Clasicos",
  "Artista" : "Porretas",
  "Año" : 2000,
  "Precio" : 20.0,
  "Genero" : "Rock"
  },
  {
  "Disco_num" : 3,
  "Nombre" : "Apocalypse Cow ",
  "Artista" : "Milk Inc",
  "Año" : 1998,
  "Precio" : 15.0,
  "Genero" : "Electro"
  },
  {
  "Disco_num" : 4,
  "Nombre" : "Pump Up The Jam",
  "Artista" : "Technotronic",
  "Año" : 1993,
  "Precio" : 38.0,
  "Genero" : "Electro"
  },
  {
  "Disco_num" : 5,
  "Nombre" : "In The Nightside Eclipse",
  "Artista" : "Emperor",
  "Año" : 1994,
  "Precio" : 55.0,
  "Genero" : "Black metal"
  },
  {
  "Disco_num" : 6,
  "Nombre" : "Passage",
  "Artista" : "Samael",
  "Año" : 1996,
  "Precio" : 62.0,
  "Genero" : "Black metal"
  },
  {
  "Disco_num" : 7,
  "Nombre" : "Icon",
  "Artista" : "Benighted",
  "Año" : 2008,
  "Precio" : 38.0,
  "Genero" : "Death metal"
  },
  {
  "Disco_num" : 8,
  "Nombre" : "Thriller",
  "Artista" : "Michael Jackson",
  "Año" : 1982,
  "Precio" : 230.0,
  "Genero" : "Pop"
  },
  {
  "Disco_num": 9.0,
  "Nombre" : "Van Halen",
  "Artista" : "Van Halen",
  "Año" : 1978,
  "Precio" : 160.0,
  "Genero" : "Metal"
  },
  {
  "Disco_num" : 10.0,
  "Nombre" : "The last Don",
  "Artista" : "Don Omar",
  "Año" : 2003,
  "Precio" : 5.0,
  "Genero" : "Reggaeton"
  }
  ]
#check 1: comprobamos que la lista se imprime correctamente
#pprint.pprint(discos)

#bucle para imprimir las lista de discos 
for idx, disc in enumerate(discos):
    print (f'Nº disco: {idx+1}:, Nombre: {disc["Nombre"]}:, Artista: {disc["Artista"]}, Precio: {disc["Precio"]}, Genero: {disc["Genero"]}')
seleccion = int(input (">Selecciona un disco y 0 para finalizar la compra: "))-1

#check 2
#print(seleccion)
#print(discos[seleccion])

precioCarrito = 0
cantidadDescuento = 0


if discos[seleccion]['Genero'] == 'Electro' or discos[seleccion]['Genero'] == 'Black metal':
    precioCarrito = discos[seleccion]['Precio']*0.7
    cantidadDescuento = discos[seleccion]['Precio']*0.3
else:
    precioCarrito = discos[seleccion]['Precio']
    

print(f'> Precio del carrito: {precioCarrito}')
print(f'> Precio descuento: {cantidadDescuento}')





