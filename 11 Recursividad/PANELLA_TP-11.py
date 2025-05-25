# ACTIVIDAD 1
def factorial_recursivo(n):
    """
    Función recursiva que calcula el factorial de un número
    Args:
        n (int): Número para calcular factorial
    Returns:
        int: Factorial de n
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

def mostrar_factoriales():
    """
    Solicita un número al usuario y muestra los factoriales desde 1 hasta ese número
    """
  
    numero = int(input('Ingrese un número entero positivo: '))
    if numero < 1:
        print('Por favor ingrese un número mayor o igual a 1')
        return
        
    print('\nFactoriales del 1 al', numero, ':')
    for i in range(1, numero + 1):
        print(f'{i}! = {factorial_recursivo(i)}')
    
mostrar_factoriales()

# ACTIVIDAD 2:

def fibonacci_recursivo(n):
    """
    Función recursiva que calcula el valor Fibonacci en la posición n
    Args:
        n (int): Posición en la serie Fibonacci (comenzando desde 0)
    Returns:
        int: Valor Fibonacci en la posición n
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def mostrar_serie_fibonacci():
    """
    Solicita una posición al usuario y muestra la serie Fibonacci completa hasta esa posición
    """
    
    posicion = int(input('Ingrese la posición hasta la que desea generar la serie Fibonacci: '))
    if posicion < 0:
        print('Por favor ingrese un número entero no negativo')
        return
        
    print(f'\nSerie de Fibonacci hasta la posición {posicion}:')
    for i in range(posicion + 1):
        print(f'Posición {i}: {fibonacci_recursivo(i)}')
    
mostrar_serie_fibonacci()

# ACTIVIDAD 3

def potencia_recursiva(base, exponente):
    """
    Función recursiva que calcula la potencia de un número
    utilizando la fórmula: base^exponente = base * base^(exponente-1)
    
    Args:
        base (int): Número base
        exponente (int): Exponente no negativo
        
    Returns:
        int: Resultado de base elevado a exponente
    """
    # Caso base: cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1
    # Caso base: exponente 1 retorna la misma base
    elif exponente == 1:
        return base
    # Caso recursivo
    else:
        return base * potencia_recursiva(base, exponente - 1)

def main():
    """
    Función principal que prueba la función de potencia recursiva
    """
    print('Calculadora de Potencias Recursivas')
    print('----------------------------------')
    
   
    # Solicitar datos al usuario
    base = int(input('Ingrese la base: '))
    exponente = int(input('Ingrese el exponente (entero no negativo): '))
        
    if exponente < 0:
        print('Error: El exponente debe ser un entero no negativo')
        return
        
    # Calcular y mostrar resultado
    resultado = potencia_recursiva(base, exponente)
    print(f'\nEl resultado de {base}^{exponente} es: {resultado}')
    
main()

# ACTIVIDAD 4:
def decimal_a_binario(n):
    """
    Función recursiva que convierte un número decimal a su representación binaria
    Args:
        n (int): Número entero positivo en base decimal
    Returns:
        str: Representación binaria como cadena de texto
    """
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
    
print(decimal_a_binario(10))

# ACTIVIDAD 5:

def es_palindromo(palabra):
    """
    Función recursiva que determina si una palabra es palíndromo
    Args:
        palabra (str): Cadena de texto sin espacios ni tildes
    Returns:
        bool: True si es palíndromo, False si no lo es
    """
    # Caso base: cadena vacía o de 1 carácter
    if len(palabra) <= 1:
        return True
    # Comparar primer y último carácter
    if palabra[0].lower() != palabra[-1].lower():
        return False
    # Llamada recursiva con la subcadena sin los extremos
    return es_palindromo(palabra[1:-1])

# Ejemplos de uso
print(es_palindromo('reconocer'))  # True
print(es_palindromo('Python'))     # False
print(es_palindromo('a'))          # True
print(es_palindromo(''))           # True

# ACTIVIDAD 6:

def suma_digitos(n):
    """
    Función recursiva que suma los dígitos de un número entero positivo
    Args:
        n (int): Número entero positivo
    Returns:
        int: Suma de sus dígitos
    """
    # Caso base: número de un solo dígito
    if n < 10:
        return n
    # Caso recursivo: último dígito (n % 10) + suma del resto (n // 10)
    else:
        return (n % 10) + suma_digitos(n // 10)

# Ejemplos de uso
print(suma_digitos(1234))  # Output: 10
print(suma_digitos(9))     # Output: 9
print(suma_digitos(305))   # Output: 8

# ACTIVIDAD 7:

def contar_bloques(n):
    """
    Función recursiva que calcula el total de bloques en una pirámide
    donde el nivel base tiene n bloques y cada nivel superior tiene uno menos.
    
    Args:
        n (int): Bloques en el nivel base (entero positivo)
        
    Returns:
        int: Total de bloques en la pirámide
    """
    # Caso base: si hay 1 bloque, es el último nivel
    if n == 1:
        return 1
    # Caso recursivo: bloques del nivel actual + suma de niveles superiores
    else:
        return n + contar_bloques(n - 1)

# Ejemplos de uso
print(contar_bloques(1))   # Output: 1
print(contar_bloques(2))   # Output: 3
print(contar_bloques(4))   # Output: 10
print(contar_bloques(10))  # Output: 55

# ACTIVIDAD 8:

def contar_digito(numero, digito):
    """
    Función recursiva que cuenta cuántas veces aparece un dígito en un número
    Args:
        numero (int): Número entero positivo
        digito (int): Dígito a buscar (0-9)
    Returns:
        int: Cantidad de veces que aparece el dígito
    """
    # Caso base: número de un solo dígito
    if numero < 10:
        return 1 if numero == digito else 0
    # Caso recursivo: contar en último dígito + contar en el resto
    ultimo_digito = numero % 10
    resto_numero = numero // 10
    return (1 if ultimo_digito == digito else 0) + contar_digito(resto_numero, digito)

# Ejemplos de uso
print(contar_digito(12233421, 2))  # Output: 3
print(contar_digito(5555, 5))      # Output: 4
print(contar_digito(123456, 7))    # Output: 0