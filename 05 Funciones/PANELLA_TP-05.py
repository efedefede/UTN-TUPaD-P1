import math

# ACTIVIDAD 1:
def imprimir_hola_mundo():
    print('Hola Mundo!')

# ACTIVIDAD 2:
def saludar_usuario(nombre):
    print(f'Hola {nombre}!')

# ACTIVIDAD 3:
def informacion_personal(nombre, apellido, edad, residencia):
    print(f'Soy{nombre} {apellido}, tengo {edad} años y vivo en {residencia}')

# ACTIVIDAD 4:
def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

# ACTIVIDAD 5:
def segundos_a_horas(segundos):
    horas = segundos / 3600 
    return horas

# ACTIVIDAD 6:
def  tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# ACTIVIDAD 7:
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else 'Indefinido (división por cero)'
    
    print(f'Suma: {a} + {b} = {suma}')
    print(f'Resta: {a} - {b} = {resta}')
    print(f'Multiplicación: {a} * {b} = {multiplicacion}')
    print(f'División: {a} / {b} = {division}')
    
    return (suma, resta, multiplicacion, division) 

# ACTIVIDAD 8:
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# ACTIVIDAD 9:
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# ACTIVIDAD 10:
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio




# DEFINICIÓN DE FUNCIÓN PRINCIPAL:
def main():
    nombre = input('Ingrese su nombre')
    apellido = input('Ingrese su apellido')
    edad = int(input('Ingrese su edad'))
    residencia = input('Ingrese su lugar de residencia')

    imprimir_hola_mundo()
    saludar_usuario(nombre)
    informacion_personal(nombre, apellido, edad, residencia)

    radio = float(input('Ingrese el radio del círculo: '))
    print(f'Área: {calcular_area_circulo(radio):.2f}')
    print(f'Perímetro: {calcular_perimetro_circulo(radio):.2f}')

    segundos = int(input('Ingrese la cantidad de segundos'))
    print(f'La cantidad de segundos ingresados equivalen a: {segundos_a_horas(segundos):.2f} horas')

    numero = int(input('Ingrese un número: '))
    tabla_multiplicar(numero) 

    num1 = int(input('Ingrese un número: '))
    num2 = int(input('Ingrese otro número: '))
    resultado = operaciones_basicas(num1, num2)
    print(f'Tupla devuelta {resultado}')

    peso = float(input('Ingrese su peso en kilogramos: '))
    altura = float(input('Ingrese su altura en metros: '))
    resultado_imc = calcular_imc(peso, altura)
    print(f'Su Índice de Masa Corporal (IMC) es: {resultado_imc:.2f}')

    temperatura_celsius = float(input('Ingrese la temperatura en grados Celsius: '))
    temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
    print(f'{temperatura_celsius}°C equivalen a {temperatura_fahrenheit}°F') 

    numA = int(input('Ingrese un número: '))
    numB = int(input('Ingrese otro número: '))
    numC = int(input('Ingrese otro número mas: '))
    promedio = calcular_promedio(numA, numB, numC)
    print(f'El promedio de esos 3 número es: {promedio}')
    

# LLAMADO DE LA FUNCIÓN PRINCIPAL:
main()