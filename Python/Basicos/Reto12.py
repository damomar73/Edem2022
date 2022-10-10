#reto 12 - NIVEL FACIL
def retof12(numero_alum):
  nombres=[]
  for x in range(numero_alum):
    nom = input("> Indica el nombre del alumn@ del curso Programacion para No Programadores: ")
    nombres.append(nom)
  for x in range(numero_alum):
    print(nombres[x])