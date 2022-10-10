#reto 5 - NIVEL FACIL
def retof5():
  pwd:str = input ("Introduce una contraseña: ")
  while pwd != 'admin':
    pwd:str = input ("Introduce otra contraseña: ")
  if pwd == 'admin':
      print (f"> Bienvenido al programa señor {pwd.upper()}")

