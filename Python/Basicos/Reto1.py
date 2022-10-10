#reto 1 - NIVEL FACIL
'''
def retof1():
  nombre:str = "David"
  apellidos:str = "Moreno Martinez"
  edad:int = 48
  mail:str = "damomar73@gmail.com"
  telefono:int = 649541181
  casado:bool = True
  con_hijos:bool = True
  amigos:list = ["Raul", "Cote", "Dani"]
  peliculas:dict = {
    "p1":"La vida es bella",
    "p2":"Los Goonies",
    "p3":"Alien"
     }
  print(f"> Nombre: " + nombre)
  print(f"> Apellidos: " + apellidos)
  print(f"> Edad: {edad}")
  print(f"> Mail: " + mail)
  print(f"> Telefono: {telefono}")
  print(f"> Casado: {casado}")
  print(f"> Con hijos: {con_hijos}")
  print(f"> Amigos: {amigos}")
  print(f"> Peliculas: {peliculas}")
  '''
def retof1():

  datos_contacto = {
  "nombre" : "David",
  "apellidos" : "Moreno Martinez",
  "edad" : 48,
  "mail" : "damomar73@gmail.com",
  "telefono" : 649541181,
  "casado" : True,
  "con_hijos" : True,
  "amigos" : ["Raul", "Cote", "Dani"],
  "peliculas" : {
    "p1":"La vida es bella",
    "p2":"Los Goonies",
    "p3":"Alien"
     }}
  print(datos_contacto)