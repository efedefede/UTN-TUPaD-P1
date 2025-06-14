# ACTIVIDAD 1:
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas.update({'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300})
print(precios_frutas)

# ACTIVIDAD 2:
precios_frutas.update({'Banana': 1330, 'Manzana': 1700, 'Melón': 2800})
print(precios_frutas)

# ACTIVIDAD 3:
frutas = list(precios_frutas.keys())
print(frutas)

# ACTIVIDAD 4:
contactos = {}
for _ in range(5):
    nombre = input('Ingrese nombre del contacto: ')
    telefono = input('Ingrese número telefónico: ')
    contactos[nombre] = telefono

consulta = input('Ingrese nombre a consultar: ')
print(contactos.get(consulta, 'Contacto no encontrado'))

# ACTIVIDAD 5:
frase = input('Ingrese una frase: ')
palabras = frase.split()
unicas = set(palabras)
recuento = {palabra: palabras.count(palabra) for palabra in unicas}

print('Palabras únicas:', unicas)
print('Recuento:', recuento)

# ACTIVIDAD 6:
alumnos = {}
for _ in range(3):
    nombre = input('Nombre del alumno: ')
    notas = tuple(float(input(f'Nota {i+1}: ')) for i in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas)/len(notas)
    print(f'{nombre}: {promedio:.2f}')

# ACTIVIDAD 7:

parcial1 = {'Ana', 'Juan', 'María', 'Carlos'}
parcial2 = {'Juan', 'Pedro', 'María'}

print('Aprobaron ambos:', parcial1 & parcial2)
print('Aprobaron solo uno:', parcial1 ^ parcial2)
print('Aprobaron al menos uno:', parcial1 | parcial2)

# ACTIVIDAD 8:
stock = {'Lápiz': 50, 'Cuaderno': 30, 'Goma': 20}

while True:
    producto = input('Producto (o "salir"): ')
    if producto.lower() == 'salir':
        break
    
    if producto in stock:
        print(f'Stock actual: {stock[producto]}')
        opcion = input('¿Agregar unidades? (s/n): ')
        if opcion.lower() == 's':
            unidades = int(input('Cantidad a agregar: '))
            stock[producto] += unidades
    else:
        unidades = int(input('Nuevo producto. Ingrese stock inicial: '))
        stock[producto] = unidades
    
    print('Stock actualizado:', stock)

# ACTIVIDAD 9:
agenda = {
    ('lunes', '10:00'): 'Reunión',
    ('martes', '15:00'): 'Clase de inglés'
}

dia = input('Día (ej. lunes): ')
hora = input('Hora (ej. 10:00): ')
print(agenda.get((dia, hora), 'No hay eventos programados'))

# ACTIVIDAD 10
paises = {'Argentina': 'Buenos Aires', 'Chile': 'Santiago', 'Brasil': 'Brasilia'}
capitales = {capital: pais for pais, capital in paises.items()}
print(capitales)