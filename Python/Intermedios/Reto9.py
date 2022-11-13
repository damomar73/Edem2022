"""Función que convierte un número binario en decimal.
    Parámetros:
        n: Es una cadena de ceros y unos
    Devuelve:
        El número decimal correspondiente a n
"""

b = str (input ("> Introduce un nº binario: "))
def to_decimal(b):
    b = list(b)
    b.reverse()
    decimal = 0
    for i in range(len(b)):
        decimal += int(b[i]) * 2 ** i
    return decimal

"""Función que convierte un número decimal en binario.
    Parámetros:
        n: Es un número entero
    Devuelve:
        El número binario correspondiente a n
"""

n = int (input ("> Introduce un nº entero: "))
def to_binary(n):  
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n //= 2
    binary.reverse()
    return ''.join(binary)

if __name__ == "__main__":
    print(to_decimal(b))
    print(to_binary(n))
