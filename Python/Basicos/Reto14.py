#reto 14 - NIVEL FACIL
from math import pi

def areaC():
  radio = float (input ("> Introduce el radio del cilindro (cm): "))
  global areaCir
  areaCir = float (pi * (radio ** 2))
  print (f'> El area del circulo es:  {areaCir} cm2')

def volumenC(alturaC: float)-> float:
  volumenC = areaCir * alturaC
  print (f'> El volumen del cilindro es: {volumenC} cm2')