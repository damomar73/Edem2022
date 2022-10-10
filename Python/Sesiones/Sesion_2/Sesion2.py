'''
PALABRAS RESERVADAS DE PYTHON

- and
- as
- assert
- break
- class (declarar tipos propios)
- continue
- def (manera de definir una funcion)
- del
- elif
- else
- except
- exec
- finally
- for
- global (definir variables de ambito superior al archivo)
- if
- import (importar modulos que se exportan de una libreria)
- in
- is
- lambda
- nonlocal
- not
- or
- pass
- raise
- return
- try
- while
- with
- yield
- True
- False
- None
'''

numeroElegido = int(input("Elige un número: "))
numeroBuscado = 300
intentos = 3

'''
while(numeroElegido % 2 != 0):
  numeroElegido = int(input("Vuelve a elegir un número: "))
'''

while(numeroElegido != numeroBuscado):
  if(numeroElegido > numeroBuscado):
    numeroElegido = int(input("Has fallado, el número buscado es más pequeño: "))
  else:
    numeroElegido = int(input("Has fallado, el número buscado es más grande: "))

print(f"Has ganado, el número era {numeroBuscado}")

#ver el orden y que sale en impresion
operacion_compleja = 33 * 10 + 2 / 5 ** 2
print(f"> Operación 33*10+2/5**2 = {operacion_compleja}")

nombre: str = "Martín"
apellidos: str = "San José de Vicente" 

# Concatenación
nombre_completo: str = nombre + " " + apellidos
print(f"> Nombre completo: {nombre_completo}")  

# Repetición
nombre_x5: str = nombre*5
print(f"> Nombre 5 veces: {nombre_x5}")

c: int = 3
d: int = 3
e: int = 4

# Igualdad - Nos devolverá True o False
print(f"> ¿3 y 3 son iguales? {c is d}") 
# Operador Identidad
print(f"> ¿3 y 3 son iguales? {c == d}")
print(f"> ¿3 y 4 son iguales? {c is e}") # Operador Identidad

print(f"¿3 mayor que 2? {3 > 2}")

print(f"Verdadero y Verdadero = {True and True}")
print(f"Verdadero y 1 = {True and 1}")
print(f"> Falso y 0 = {False and 0}")
	
print(f"Not Verdadero = {not True}")
print(f"Not Falso = {not False}")
print(f"Not Falso o Verdadero = {not (False or True)}")

mi_texto:str = "Lorem ipsum dolor sit amet consectetur adipiscing elit dui odio"
mi_sub_texto: str = "amet"
mi_otro_sub_texto: str = "pepito"

print(f"> ¿amet está dentro del mi_texto?: {mi_sub_texto in mi_texto}")
print(f"> ¿pepito no está dentro de mi_texto?: {mi_otro_sub_texto not in mi_texto}")

edad = 30
edad += 1

puntos_obtenidos: int = 0

print(f"> Los puntos obtenidos actuales son: {puntos_obtenidos}")
puntos_obtenidos = puntos_obtenidos + 1
print(f"> Los puntos obtenidos actuales son: {puntos_obtenidos}")

#hace lo mismo que el codigo de arriba pero en una sola linea
puntos_obtenidos += 1
print(f"> Has conseguido otro punto. Ahora tienes: {puntos_obtenidos}")

'''
EJERCICIO
- Por consola el usuario debe acertar un número secreto
- Tiene 3 intentos
- Si acierta en el primer intento: Se suman 5 puntos y el resultado se multiplican por 2
- Si acierta en el segundo intento: Se suman 5 puntos
- Si acierta a la tercera: Se suma 2 puntos
- Si falla todas las veces: Se resta 2 puntos
'''