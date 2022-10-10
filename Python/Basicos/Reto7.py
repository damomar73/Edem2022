#reto 7 - NIVEL FACIL

def retof7():
  password = str (input ("Introduce la contraseña: "))
  text = str (input ("Introduce un texto: "))
  pwdlow = password.lower()
  textlow = text.lower()
  if(pwdlow == textlow):
    print("> Son cadenas de texto iguales")
  else:
    print("> Son cadenas de texto distintas")