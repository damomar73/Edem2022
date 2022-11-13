def palindromo():
    cadenaTexto= str(input ("> Introduce una palabra: "))
    if cadenaTexto == cadenaTexto[::-1]:
      print("> La palabra es un palindromo")
    else:
      print("> La palabra es no es un palindromo")

if __name__ == "__main__":
  palindromo()