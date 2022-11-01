#reto 13 - NIVEL FACIL

#importamos el numero pi de la libreria math
from math import pi

def areaT():
  baseT = float(input("> Introduce la base del triangulo: "))
  alturaT = float(input("> Introduce la altura del triangulo: "))
  areaTri = (baseT * alturaT / 2)
  print (f'> El area del triangulo es:  {areaTri} cm2')

def areaC():
  radio = float(input("> Introduce el radio del circulo: "))
  areaCir = pi * (radio ** 2)
  print (f'> El area del circulo es:  {areaCir} cm2')

if __name__ == "__main__":   
  areaT()
  areaC()