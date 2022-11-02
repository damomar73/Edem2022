#reto 13 - NIVEL FACIL

# importamos el nº pi de la libreria math
from math import pi

#introducimos los datos desde consola
baseT = float(input('> Introduce la base del circulo: '))
alturaT = float(input('> Introduce la altura del circulo: '))
radio = float(input('> Introduce el radio del circulo: '))

#definimos la funcion de calculo de area del triangulo
def areaT(baseT, alturaT):
  areaTri = baseT * alturaT / 2
  print (f'> El area del triangulo es:  {areaTri} cm2')

#definimos la funcion de calculo del area del circulo
def areaC (radio):
  areaCir = pi * (radio ** 2)
  print (f'> El area del circulo es:  {areaCir} cm2')

if __name__ == "__main__":
  areaT(baseT, alturaT)
  areaC(radio)