import requests
'''
#otra forma de hacerlo pero tipando
from requests.models import Response
respuesta : Response = requests.get(url = URL)
'''
	
def obtenerChiste():
  URL = 'https://api.chucknorris.io/jokes/random'
  #forma de conseguir un objeto, en este caso "respuesta"
  respuesta = requests.get(url = URL)
  status = respuesta.status_code
  if status >= 200 and status <= 300:
    # Devuelve en contenido en formato JSON de "respuesta"
    datos = respuesta.json()
    # Obtenemos valor en la clave 'value' del JSON que nos interesa
    frase_chuck: str = datos['value']	
    # Imprimimos el chiste por consola
    return frase_chuck
  else:
    return "Status erroneo"