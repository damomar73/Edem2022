'''
#version larga y "bonita" - 20 lineas
numeroElegido = int(input(">Elige un número entre 1 y 100: "))
numeroBuscado = 73
intentos: int = 1
puntos_obtenidos: int = 5
while(numeroElegido != numeroBuscado):
  if(numeroElegido > numeroBuscado):
    numeroElegido = int(input(">Has fallado, el número buscado es más pequeño: "))
    intentos +=1
  else:
    numeroElegido = int(input(">Has fallado, el número buscado es más grande: "))
    intentos +=1
if intentos == 1:
   puntos_obtenidos = puntos_obtenidos * 2
elif intentos == 2:
  puntos_obtenidos = puntos_obtenidos 
elif intentos == 3:
  puntos_obtenidos = puntos_obtenidos -3
else:
  puntos_obtenidos = puntos_obtenidos - 7
print(f">Has ganado, el número era {numeroBuscado} y los puntos obtenidos actuales son: {puntos_obtenidos}")
'''

#version corta - 14 lineas
numeroElegido = int(input(">Elige un número entre 1 y 100: "))
numeroBuscado = 73
intentos: int = 0
puntos_obtenidos: int = 10
while(numeroElegido != numeroBuscado):
  intentos +=1  
  if intentos == 1:
    puntos_obtenidos = puntos_obtenidos -5
  elif intentos == 2:
    puntos_obtenidos = puntos_obtenidos -3
  else:
    puntos_obtenidos = -2
  numeroElegido = int(input(">Has fallado, pon otro numero: "))
print(f">Has ganado, el número era {numeroBuscado} y los puntos obtenidos actuales son: {puntos_obtenidos}")

'''
EJERCICIO
- Por consola el usuario debe acertar un número secreto
- Tiene 3 intentos
- Si acierta en el primer intento: Se suman 5 puntos y el resultado se multiplican por 2
- Si acierta en el segundo intento: Se suman 5 puntos
- Si acierta a la tercera: Se suma 2 puntos
- Si falla todas las veces: Se resta 2 puntos
'''