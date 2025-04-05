import random 
from statistics import mode, median, mean 

# Actividad 1:
edad = int(input('Ingrese su edad: '))
if edad > 18:
    print('Es mayor de edad')


# Actividad 2:
nota = float(input('Ingrese su nota: '))
if nota >= 6:
    print('Aprobado')
else:
    print('Desaprobado')

# Actividad 3:
numero = int(input('Ingrese un número par: '))
mensaje = 'Ha ingresado un número par' if numero % 2 == 0 else 'Por favor, ingrese un número par'
print(mensaje)

# Actividad 4:
edad = int(input('Ingrese su edad: '))
if edad < 12:
    print('Niño/a')
elif edad >= 12 and edad < 18:
    print('Adolescente')
elif edad >= 18 and edad < 30:
    print('Adulto/a joven')
else:
    print('Adulto/a')

#Actividad 5:
password = input('Ingrese una contraseña: ')
length = len(password)

if length >= 8 and length <= 14:
    print('Ha ingresado una contraseña correcta')
else:
    print('Por favor, ingrese una contraseña de entre 8 y 14 caracteres')

#Actividad 6:
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana > moda:
    print('Sesgo positivo o a la derecha')
elif media < mediana < moda:
    print('Sesgo negativo o a la izquierda')
elif media == mediana == moda:
    print('No hay sesgo')

#Actividad 7:
entrada = input('Ingrese una frase o palabra: ')
vocales = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']

if entrada and entrada[-1].lower() in vocales:
    print(entrada + '!')
else:
    print(entrada) 

#Actividad 8:
nombre = input('Ingrese su nombre: ')
numero = int(input('Ingrese un número: ' \
'1. Si quiere su nombre en mayúsculas.' \
'2. Si quiere su nombre en minúsculas.' \
'3. Si quiere su nombre con la primera letra mayúscula'))

if numero == 1:
    print(nombre.upper())
elif numero == 2:
    print(nombre.lower())
elif numero == 3:
    print(nombre.title())
else:
    print('El número debe ser 1, 2 ó 3')

#Actividad 9:
magnitud = float(input('Ingrese la magnitud del terremoto: '))

if magnitud < 3:
    print('Muy leve')
elif magnitud < 4:
    print('Leve' )
elif magnitud < 5:
    print('Moderado')
elif magnitud < 6:
    print('Fuerte')
elif magnitud < 7:
    print('Muy Fuerte')
else:
    print('Extremo')

#Atividad 10:
hemisferio = input("¿En qué hemisferio te encuentras? (N para Norte / S para Sur): ")
mes = int(input("Ingresa el mes (1-12): "))
dia = int(input("Ingresa el día (1-31): "))

if hemisferio.upper() == 'N':
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print('Invierno')
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print('Primavera') 
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print('Verano') 
    else:
        print('Otoño') 
elif hemisferio.upper() == 'S':
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print('Verano') 
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print('Otoño') 
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print('Invierno') 
    else:
        print('Primavera') 
else:
    print('Hemisferio no válido') 

