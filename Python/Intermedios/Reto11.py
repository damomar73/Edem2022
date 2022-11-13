#reto 11 - NIVEL INTERMEDIO/AVANZADO

def nif():
#creamos el diccionario clientes vacio    
  clientes = {}
#por defecto la opcion elegida es 0 para poder entrar en el bucle while
  opcion = 0
#mientras la opcion elegida no sea 6 entramos en el bucle, en caso contrario finaliza el programa
  while opcion != '6':
#introducimos los datos del usuari@
    if opcion == '1':
        nif = str(input('> Introduce el NIF del cliente: '))
        nombre = str(input('> Introduce el nombre del cliente: '))
        apellidos = str(input('> Introduce los apellidos del cliente: '))
        telefono = str(input('> Introduce el teléfono del cliente: '))
        email = str(input('> Introduce el email del cliente: '))
        preferente = input('> ¿Es un cliente preferente (S/N)? ')
#si el cliente es preferente se debera introducir la opcion S en caso contrario no es preferente
        if preferente == 'S':
            preferente = True
            cliente = {'nombre':nombre, 'apellidos':apellidos, 'teléfono':telefono, 'email':email, 'preferente':preferente}
        else:
            preferente = False
            cliente = {'nombre':nombre, 'apellidos':apellidos, 'teléfono':telefono, 'email':email, 'preferente':preferente}
#hacemos un check para saber si se gurda bien si un cliente es preferente o no
        #print(preferente)
#creamos la clave nif asociada a todos los valores de los clientes: nombre, apellidos, telefono, email y si es VIP o no
        clientes[nif] = cliente
#con la opcion 2 eliminamos los clientes de la base de datos segun el NIF introducido
    if opcion == '2':
        nif = input('> Introduce NIF del cliente: ')
        if nif in clientes:
            del clientes[nif]
        else:
            print(f'> No existe ningun cliente con el NIF: {nif}')
#con la opcion 3 mostramos los clientes segun su NIF
    if opcion == '3':
        nif = input('> Introduce NIF del cliente: ')
        if nif in clientes:
            print('NIF:', nif)
            for clave, valor in clientes[nif].items():
                print(clave.title() + ':', valor)
        else:
            print(f'> No existe ningun cliente con el NIF: {nif}')
#con la opcion 4 mostramos todos los clientes con NIF, nombre y apellidos
    if opcion == '4':
        print('> Lista de clientes: ')
        for clave, valor in clientes.items():
            print(clave, valor['nombre'], valor['apellidos'])
#con la opcion 5 mostramos solo los clientes preferentes con su NIF, nombre y apellidos
    if opcion == '5':
        print('> Lista de clientes preferentes: ')
        for clave, valor in clientes.items():
            if valor['preferente']:
                print(clave, valor['nombre'], valor['apellidos'])
#aqui mostramos por pantalla las distintas opciones a elegir por el usuari@
    opcion = input('MENU OPCIONES\n(1) Añadir un cliente\n(2) Eliminar cliente por NIF\n(3) Mostrar cliente por NIF\n(4) Mostrar TODOS los clientes\n(5) Mostrar UNICAMENTE los clientes preferentes\n(6) Finalizar programa\n> Elige una opción: ')
    
if __name__ == "__main__":
    nif()