#muestra todos los modulos que por defecto tiene python
#help('modules')
#como importar modulos (2 formas distintas equivalentes)
import math
import math as mate
#importamos el modulo cordialidad que hemos creado 
#utilidades e interacciones son paquetes, cordialidad es modulo y saludar es funcion
from utilidades.interaciones.cordialidad import saludar, despedida
#otra forma de importar llamamdolo frases
import utilidades.interaciones.cordialidad as frases

from utilidades.kpis import puntuacion
import pandas

#from utilidades.kpis import * (no recomendable los *)
puntos = puntuacion(0)
print(f'{saludar("Pedro")} tu puntuación es de {puntos}')

x = math.cos(200)
y = mate.cos(200)
print(x)
print(y)
numero : int = 16
print(f'La raiz cuadrada de {numero} es {mate.isqrt(numero)}')
print(f'La raiz cuadrada de {numero} es {mate.sqrt(numero)}')
#nos traemos lo que necesitamos con lo que no hace falta llamar a mate, antes de esta linea no se puede usar sin, tan etc ya que no se han importado
from math import sqrt, isqrt, sin, tan
sqrt(200)
sin(200)
#renombramos el modulo tan como tangente
from math import tan as tangente
tangente(300)
#si queremos importar TODO y no hace falta llamarlos con math.XXXX
from math import *

'''
#ejemplo ejecucion saludar del archico cordialidad.py
saludo = saludar('martin')
print(saludo)
despedida = despedida('Martin')
print(despedida)
'''

'''
saludo = frases.saludar('martin')
print(saludo)
despedida = frases.despedida('Martin')
print(despedida)
'''

print(f'Ptos obtenidos: {puntuacion(5)}')