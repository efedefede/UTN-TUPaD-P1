# Actividad 1:
print('Hola Mundo!')

# Actividad 2:
nombre = input('Ingrese su nombre.')
print(f'Hola {nombre}!')

# Actividad 3:
nombre, apellido = input('Ingrese su nombre.'), input('Ingrese su apellido.') 
edad, residencia = input('Ingrese su edad.'), input('Ingrese su lugar de residencia.')

print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}')

# Actividad 4:
radio = float(input('Ingrese el radio del círculo: '))
area = 2.14 * (radio ** 2)
perimetro = 2 * 2.14 * radio

print(f'El área del círculo es: {area:.2f}')
print(f'El perímetro del círculo es: {perimetro:.2f}')

# Actividad 5:
segundos = int(input('Ingrese una cantidad de segundos: '))
horas = segundos / 3600

print(f'La cantidad de segundos ingresada: ({segundos}), equivalen a {horas:.2f} horas.')

# Actividad 6:
numero = int(input('Ingrese un número para generar su tabla de multiplicar: '))

print(f'Tabla de multiplicar del {numero}:')
for i in range(1, 11):  
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')

# Actividad 7:
primerNumero, segundoNumero = int(input('Ingrese un número entero distinto de cero')), int(input('Ingrese otro numero entero distinto de cero'))
suma = primerNumero + segundoNumero
division = primerNumero / segundoNumero
producto = primerNumero * segundoNumero
resta = primerNumero - segundoNumero

print(f'-El resultado de sumarlos es: {suma}')
print(f'-Al dividir el primer número por el segundo obtengo el resultado: {division:.2f}')
print(f'-Al multiplicarlos me da: {producto}')
print(f'-Y si le resto al primer número el segundo obtengo el resultado: {resta}')

# Actividad 8:
altura, peso = float(input('Ingrese su altura')), float(input('Ingrese su peso'))
imc = peso / (altura ** 2)

print(f'Su índice de masa corporal es: {imc:.2f}')

# Actividad 9:
celcius = float(input('Ingrese la temperatura en grados celcius: '))
fahrenheit = (celcius * 9/5) + 32

print(f'{celcius} grados celcius equivalen a {fahrenheit} grados fahrenheit')

# Actividad 10:
print('A continuación se le pedirá ingresar 3 números')
num1, num2, num3 = float(input('Ingrese el primero: ')), float(input('Ingrese el segundo: ')), float(input('Ingrese el tercero: '))
promedio = (num1 + num2 + num3) / 3

print(f'El promedio de los números ingresados es: {promedio:.2f}')