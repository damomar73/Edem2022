#reto 9 - NIVEL FACIL
def retof9(year):
  if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
      print('> Ese año es bisiesto')
  else:
    print('> Ese año no es bisiesto')