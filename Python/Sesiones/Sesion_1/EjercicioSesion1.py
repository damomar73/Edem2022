#introduccion datos por usuario
name = input("Dime tu nombre: ")
mail = input ("Dime tu mail: ")
pasword = input ("Dime tu contraseña: ")
age = input ("Dime tu edad: ")

#creacion del diccionario
datos = {
  "Nombre": name,
  "Mail": mail,
  "Contraseña": pasword,
  "Edad": age
}

#impresion diccionario
for x, y in datos.items():
    print(x, y)
  
#otra forma de imprimir mas visual
print(f'''Nombre: {datos["Nombre"]}
Mail: {datos["Mail"]} 
Contraseña: {datos["Contraseña"]} 
Edad: {datos["Edad"]}''')