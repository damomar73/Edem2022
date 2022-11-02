#reto 14 - NIVEL FACIL

# importamos el nº pi de la libreria math
from math import pi

#definimos la funcion de calculo de area del circulo
def areaC():
  radio = float(input ("> Introduce el radio del cilindro (cm): "))
  #asignamos una varible global para poder utilizarla en la siguiente funcion
  global areaCir
  areaCir = pi * (radio ** 2)
  print (f'> El area del circulo es:  {areaCir} cm2')

#introducimos la altura del cilindro
alturaC = float(input ("> Introduce la altura del cilindro (cm): "))

#definimos la funcion de calculo del volumen del cilindro
def volumenC(alturaC):
  volumenC = areaCir * alturaC
  print (f'> El volumen del cilindro es: {volumenC} cm2')

if __name__ == "__main__":
  areaC()
  volumenC(alturaC)