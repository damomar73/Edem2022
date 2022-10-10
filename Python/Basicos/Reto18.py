#reto 18 - NIVEL FACIL
def eliminar(palabra:str,posicion:int):
  print (palabra[0:posicion:] + palabra[posicion+1::]) 