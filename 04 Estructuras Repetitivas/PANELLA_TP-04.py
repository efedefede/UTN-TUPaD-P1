import random

#ACTIVIDAD 1:
for x in range(101):
    print(x)

#ACTIVIDAD 2:
num = input('Ingrese un número entero: ')
print(f'La cantidad de dígitos es {len(num)}')

#ACTIVIDAD 3:
firstValue = int(input('ingrese un número entero: '))
secondValue = int(input('ingrese un número entero mayor al anterior: '))

sume = 0
for x in range(firstValue+1, secondValue):
    sume += x

print(f'La sumatoria entre estos dos valores (excluyéndolos) es: {sume}')

#ACTIVIDAD 4:
suma = 0
num = int(input('ingrese un número entero (si ingresa cero la el programa se detendrá) '))

while num != 0:
    suma += num
    num = int(input('ingrese otro (cero para detenerse) '))

print(f'El resultado de la sumatoria es: {suma}')

#ACTIVIDAD 5:
num = random.randint(0, 9)
userNum = int(input('Ingrese un número entre cero y nueve '))
trys = 0

while num != userNum:
    trys += 1
    userNum = int(input('Incorrecto, ingresa otro '))

print(f'Correcto, adivinaste en {trys} intentos!')

#ACTIVIDAD 6:
for x in range(100, 0, -2):
    print(x)

#ACTIVIDAD 7:
sume = 0
num = int(input('Ingrese un número entero: '))

for x in range(num + 1):
    sume += x

print(f'La sumatoria es: {sume}')

#ACTIVIDAD 8:
pares = impares = positivos = negativos = 0

for cont in range(5):
    numero = int(input('ingrese un número entero: '))
    if numero % 2 == 0:
        pares += 1
    else: 
        impares += 1
    
    if numero > 0:
        positivos += 1
    else: 
        negativos += 1

print(f'ingresaste {pares} números pares, {impares} números impares, {positivos} positivos y {negativos} negativos')

#ACTIVIDAD 9:
sumatoria = 0
limite = 10

for cont in range(limite):
    numeroEntero = int(input('ingrese un número entero: '))
    sumatoria += numeroEntero

media = sumatoria / limite
print(f'La media es {media:.2f}')

#ACTIVIDAD 10:
numStrFromUser = input('Ingrese un número entero: ')
numStrResult = ''

for cont in range(len(numStrFromUser) - 1, -1, -1):
    numStrResult = numStrResult + numStrFromUser[cont]

print(numStrResult)