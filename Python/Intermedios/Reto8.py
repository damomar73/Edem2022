""" Función que calcula el factorial de un número entero positivo
    Parámetros
         n: Es un entero positivo
         Devuelve el factorial de n
"""

def factorial(): 
    t = 1
    n = int (input ("> Introduce un nº entero: "))
    for i in range(n):
        print(i)
        t *= i+1
    print (f"> El factorial de {n} es: {t}")

if __name__ == "__main__":
    factorial()
