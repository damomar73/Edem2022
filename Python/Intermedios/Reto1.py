#reto 1 - NIVEL INTERMEDIO/AVANZADO

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
#pprint.pprint(discos)

#bucle para imprimir las lista de discos 
for idx, disc in enumerate(discos):
    print(f'> Nº disco: {idx+1} > Disco: {disc["Nombre"]} > Artista: {disc["Artista"]} > Precio: {disc["Precio"]} > Genero: {disc["Genero"]}')
seleccion2 = int(input ("> Selecciona un disco y 0 para finalizar la compra: "))-1

#check 2
#print(seleccion)
#print(discos[seleccion])

precioCarrito = 0
cantidadDescuento = 0

'''
if discos[seleccion]['Genero'] == 'Electro' or discos[seleccion]['Genero'] == 'Black metal':
    precioCesta = discos[seleccion]['Precio']*0.7
    cantidadDescuento = discos[seleccion]['Precio']*0.3
else:
    precioCesta = discos[seleccion]['Precio']
    
print(f'> Precio de la cesta: {precioCesta}€')
print(f'> Precio del descuento: {cantidadDescuento}€')
'''

PrecioTotalCesta = [precioCarrito]
DescuentoTotal = [cantidadDescuento]


while seleccion2 != -1:
  if discos[seleccion2]['Genero'] == 'Electro' or discos[seleccion2]['Genero'] == 'Black metal':
    precioCesta2 = discos[seleccion2]['Precio']*0.7
    cantidadDescuento2 = discos[seleccion2]['Precio']*0.3
    PrecioTotalCesta.append(precioCesta2)
    DescuentoTotal.append(cantidadDescuento2)
  else:
    precioCesta2 = discos[seleccion2]['Precio']
    PrecioTotalCesta.append(precioCesta2)
  seleccion2 = int(input ("> En caso de querer comprar otro disco selecciona otro numero o pulsa 0 para finalizar la compra: "))-1

totalCesta = sum(PrecioTotalCesta)
totalDto = sum(DescuentoTotal)
fecha = datetime.today().strftime('%d-%m-%Y')

print(f'> Fecha: {fecha}')
print(f'> Precio Total de la cesta: {totalCesta}€')
print(f'> Precio Total del descuento: {totalDto}€')