#reto 11 - NIVEL FACIL
def retof11 ():
  titulofilm = str (input ('Introduce el titulo de la pelicula: '))
  directorfilm = str (input ('Introduce el director de la pelicula: '))
  anyofilm = int (input ('Introduce el año de la pelicula: '))
  paisfilm = str (input ('Introduce el pais de la pelicula: '))
  global pelicula 
  pelicula = (titulofilm, directorfilm, anyofilm, paisfilm)
  print (*pelicula)