#reto 8 - NIVEL FACIL
def retof8(num):
  for n in range(2, num):
    if num % n == 0:
      print("No es primo")
      return False
  print("Es primo")
  return True