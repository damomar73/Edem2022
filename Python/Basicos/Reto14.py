#reto 14 - NIVEL FACIL

#importamos el numero pi de la libreria math
from math import pi

def areaC():
  radio = float (input ("> Introduce el radio del cilindro (cm): "))
  global areaCir
  areaCir = pi * (radio ** 2)
  print (f'> El area del circulo es:  {areaCir} cm2')

def volumenC():
  alturaC = float(input("> Introduce la altura del cilindro: "))
  volumenC = areaCir * alturaC
  print (f'> El volumen del cilindro es: {volumenC} cm2')

if __name__ == "__main__":
  areaC()
  volumenC()