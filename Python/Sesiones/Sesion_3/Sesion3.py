'''En Python, la estructura es con "elif" y no con "else if"'''

miEdad = 45
if (miEdad >= 60):    
  print('Apuntarse al gym')
elif (miEdad < 60 and miEdad > 30): 
#aqui hay varias anidaciones elif + if + else y vuelve a elif
  if miEdad == 45:
  print ('Adulto maduro')
  else:
  print("otro texto")
elif (miEdad == 30):    
  print ('Adulto en su sweet moment')
elif (miEdad < 30 and miEdad >= 18):    
  print ('Adulto joven, todo en orden')
else:    
  print ('¡A clase!')

'
#el proceso termina cuando no haya mas elementos en la lista
lista = [1,2,3,4,5,6,7,8] 
for elemento in lista:    
  if(elemento % 2 == 0):        
    print(f'{elemento} es par')    
  else:
#el pass hace que siga y continua con la ejecucion, no hace nada
    pass
#continue no rompe el bucle y solo se ejecutan los pares, salta lo que hay debajo y continua con lo siguiente que hay en el bucle
    continue
    print(f'{elemento} es impar')
#el break hace que termine la iteracion y se salga 
    break



#ejemplo de depuracion
lista = [1,2,3,4,5,6,7,8,9,10]
sumatorio = 0
iteraciones = 0

for numero in lista:
  sumatorio += numero
  #es lo mismo que sumatorio = sumatorio + numero
  iteraciones += 1
  
print(f'Suma total {sumatorio}')

#pop() quita el ultimo elemento de la lista
#pop(4) quita el elemento de la posicion 4
lista = [1,2,3,4,5,6,7,8]
while (len(lista) > 3):
  lista.pop()
  print(lista)



#definicion de una funcion
def nombre-funcion (parametros) -> tiporetorno
ejemplo
  def sumar (a:int, b:int) -> int:
  return a + b



# Función con Parámetros No Tipados
def miFuncionConParametros(a :str,b :str):    
  print(f"¡{a}, {b}!") 
# llamando la función y pasándole algunos parámetros
miFuncionConParametros('Hola', 'Mundo')
#podemos cambiar el orden de los parametros, si no ponemos nada por defecto es a y b
#todas estas son validas
miFuncionConParametros(b="hola",a="adios")
miFuncionConParametros(a="hola",b="adios")
miFuncionConParametros("hola",b="adios")
miFuncionConParametros("hola",a="adios")



# Función con muchos parámetros
def miFuncionConMultiplesParametros(*elementos) :    
  for elemento in elementos:        
    print(f"Elemento: {elemento}") 

# llamando la función y pasándole una lista de parámetros
lista: [int] = [1, 2, 3, 4, 5]
miFuncionConMultiplesParametros(lista)

#imprime cada elemento de forma individual
miFuncionConMultiplesParametros(1,2,3,4,5)
#imprime cada elemento de forma conjunta
miFuncionConMultiplesParametros([1,2,3,4,5])


'''
EJERCICIO
por consola solicitar al usuario un numero
pedir numeros hasta que usuario introduzca un año bisiesto
- es bisiesto si el año es divisible por 4
- no es bisiesto si solo es divisible entre 100
- es bisiesto si es divisible entre 400
'''


def aniobisiesto(anio:int):
    if (anio %4 == 0 and anio %100 == 0 and anio %400 == 0) or (anio %4 == 0 and anio %100 != 0):
      print(f"> El anio {anio} es bisiesto")
    else:     
      print(f"> El anio {anio} no es bisiesto")
anio = int(input("> Elige un anio: "))  
aniobisiesto(anio)


#otra solucion muy buena
def bisiesto(anyo:int) -> bool:
  bisiesto = False
  if (anyo%4 == 0 and ((anyo%100 == 0 and anyo%400 == 0) or ( anyo%100 != 0))):
    bisiesto = True
  return bisiesto
anyo = int(input("Escribe un año: "))
#Mientras sea falso que el año es bisiesto pide más años
while (not bisiesto(anyo)):
  anyo = int(input("Escribe otro año: "))
print('¡Has escrito un año bisiesto!')



#otra solucion 
def anioBisiesto(year:int)->bool:
  if (year%4 == 0 and year%100!=0) or year%400 == 0: 
    return True
anioUsuario = int(input('Introduce un año para saber si es bisiesto: '))
while anioBisiesto(anioUsuario) == None :  
  anioUsuario = int(input(f'El año {anioUsuario} no es bisiesto, prueba otra vez: ')) 
print(f'El año {anioUsuario} es bisiesto')

#nuestra solucion, la mejor
def leap_year(year: int):
    return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)
while not leap_year(int(input('introduce año: '))):
    print('ese año no es bisiesto')
print('has acertado')


''' 
PASO POR REFERENCIA
Paso de parámetros por Referencia 
- Los valores simples se pasan, por defecto, por valor
- Los valores complejos se pasan, por defecto, por referencia 

# las listas al ser complejos se pasan por referencia
# Esto quiere decir que si la función edita el parámetro,
# éste se edita también en origen 
def doblar_valores(numeros):    
  for indice,numero in enumerate(numeros):        
    numeros[indice] *= 2
#en la posicion "indice" la cual varia, multiplica por 2 su valor
'''

'''
#definiendo una variable que se va a pasar por referencia
ns = [10,50,100]
doblar_valores(ns)
print(f"Lista Original Modificada: {ns}") 
# [20, 100, 200]

# SI NO QUEREMOS PASAR UNA LISTA COMO REFERENCIA, DEBEMOS REALIZAR UNA COPIA "AL VUELO"
# Ahora esta no se pasará por referencia, ya que haremos una copia del valor
ns = [10,50,100]
doblar_valores(ns[:])  
# Una copia al vuelo de una lista se realiza con [:]
# Esto hace que la lista original no se vea modificada
print(f"Lista Original No Modificada: {ns}") 
#[10, 50, 100]


# Para aquellos tipos de datos simples, si queremos el mismo comportamiento# de paso por referencia podemos: 
# SOBRESCRIBIR EL VALOR ORIGINAL CON EL VALOR DE RETURN DE LA FUNCIÓN
def doblar_valor(numero):    
  return numero * 2 
n = 10
doblar_valor(n)
n = doblar_valor(n)
print(f"Valor original Modificado: {n}")

'''
'''
# FUNCIONES LAMBDA: Las funciones Lambda de Python son bastante habituales. 
al_cuadrado = lambda a: a**2 
es lo mismo que 
# def al_cuadrado (a):
#    return a**2
# llamando a la función lambda
print(al_cuadrado(2)) 
# imprimirá un 4
'''

#ejemplo uso librerias ya existentes
import calendar
print (f"El año 2020 es bisiesto? {calendar.isleap(2020)}")


#otras librerias
import time
import datetime
import calendar

'''
#ejercicio a realizar
- fecha y hora actual
- dia actual
- año actual
- mas actual
- numero del mes actual
- numero de la semana actual
- dia del año
- dia del mes
- dia de la semana
'''


print(f'Fecha y Hora actual: {datetime.datetime.now()}')
#año
print(f'{datetime.datetime.today().strftime("%Y")}')
#mes
print(f'{datetime.datetime.today().strftime("%B")}')
#nº mes
print(f'{datetime.datetime.today().strftime("%m")}')
#nº semana
print(f'{datetime.datetime.today().strftime("%W")}')
#dia del año
print(f'{datetime.datetime.today().strftime("%j")}')
#dia del mes
print(f'{datetime.datetime.today().strftime("%d")}')
#dia de la semana
print(f'{datetime.datetime.today().strftime("%A")}')
#sacar dia de la semana o mes concreto
print(f'Dia de la semana: {calendar.day_name[0]}')
print(f'Dia del Mes: {calendar.month_name[1]}')



miFecha = '23/09/2022'
print(f'Fecha legible: {datetime.datetime.strptime(miFecha,"%d/%m/%Y")}')