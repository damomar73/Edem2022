#reto 13 - NIVEL FACIL
from math import pi
def areaT(baseT, alturaT):
  areaTri = (baseT * alturaT / 2)
  print (f'> El area del triangulo es:  {areaTri} cm2')
def areaC (radio: float) -> float:
  areaCir = float (pi * (radio ** 2))
  print (f'> El area del circulo es:  {areaCir} cm2')