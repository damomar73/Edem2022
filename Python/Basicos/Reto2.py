#reto 2 - NIVEL FACIL
def retof2():
  start = int(input("Numero inicial: "))
  end = int(input("Numero final: "))
  impar = [impar for impar in range (start, end) if impar%2]
  print(impar)
  