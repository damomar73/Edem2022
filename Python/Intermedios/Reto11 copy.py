#reto 11 - NIVEL INTERMEDIO/AVANZADO

def nif():
  clientes = {}
  opcion = 0
  while opcion != '6':
    if opcion == '1':
        nif = str(input('> Introduce NIF del cliente: '))
        nombre = str(input('> Introduce el nombre del cliente: '))
        apellidos = str(input('> Introduce los apellidos del cliente: '))
        telefono = str(input('> Introduce el teléfono del cliente: '))
        email = str(input('> Introduce el email del cliente: '))
        preferente = input('> ¿Es un cliente VIP (Y/N)? ')
        cliente = {'nombre':nombre, 'apellidos':apellidos, 'teléfono':telefono, 'email':email, 'preferente':preferente=='Y'}
        print(preferente)
        clientes[nif] = cliente
    if opcion == '2':
        nif = input('> Introduce NIF del cliente: ')
        if nif in clientes:
            del clientes[nif]
        else:
            print(f'> No existe ningun cliente con el NIF: {nif}')
    if opcion == '3':
        nif = input('> Introduce NIF del cliente: ')
        if nif in clientes:
            print(f'> NIF: {nif}')
            for clave, valor in clientes[nif].items():
                print(clave.title() + ':', valor)
        else:
            print(f'> No existe ningun cliente con el NIF: {nif}')
    if opcion == '4':
        print(f'> Lista de clientes: ')
        for clave, valor in clientes.items():
            print(clave, valor['nombre'], valor['apellidos'])
    if opcion == '5':
        print(f'> Lista de clientes preferentes: ')
        for clave, valor in clientes.items():
            if valor['preferente']:
                print(clave, valor['nombre'],valor['apellidos'])
    opcion = input('MENU OPCIONES\n(1) Añadir un cliente\n(2) Eliminar cliente por NIF\n(3) Mostrar cliente por NIF\n(4) Mostrar TODOS los clientes\n(5) Mostrar UNICAMENTE los clientes preferentes\n(6) Finalizar programa\n> Elige una opción: ')
    
if __name__ == "__main__":
    nif()