#reto 17 - NIVEL FACIL
def retof17():
  tupla = (2,4,3,5,4,6,7,8,6,1)
  print (tupla)
  #encontrar los elementos de 3 a 5 
  print (tupla [3:6])
  #encontrar los 6 primeros elementos
  print (tupla [0:6])
  #muestra tupla desde quinto elemento hasta el final
  print (tupla [4:])
  #muestra toda la tupla haciendo uso de [:]
  print (tupla [:])
  #muestra todos los elementos desde posicion 2 a la 9 de dos en dos
  print (tupla[2:9:2])
  #devuelve la tupla con un salto cada 4 elementos
  print (tupla[::4])
  #usa un step negativo para mostrar la tupla desde la posicion 9 a la 2
  print (tupla[9::-1])  