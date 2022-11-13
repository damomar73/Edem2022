def maximo_comun_divisor(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a

def maximo_comun_divisor_recursivo(a, b):
    if b == 0:
        return a
    return maximo_comun_divisor_recursivo(b, a % b)

def minimo_comun_multiplo(a, b):
    return (a * b) / maximo_comun_divisor(a, b)

a = int (input ("> Introduce un nº entero: "))
b = int (input ("> Introduce otro nº entero: "))

if __name__ == "__main__":
    mcd = maximo_comun_divisor(a, b)
    mcd_recursivo = maximo_comun_divisor_recursivo(a, b)
    mcm = minimo_comun_multiplo(a, b)
    print(f"> El máximo común divisor de {a} y {b} es {mcd}. De manera recursiva, es {mcd_recursivo}")
    print(f"> El mínimo común múltiplo de {a} y {b} es {mcm}")