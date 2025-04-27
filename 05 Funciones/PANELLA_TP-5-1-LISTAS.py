#ACTIVIDAD 1:
multiplos_de_cuatro = list(range(4, 101, 4))
print(multiplos_de_cuatro)

#ACTIVIDAD 2:
lista = ['a','b','c','d','e']
print(lista[-1])

#ACTIVIDAD 3:
lista_vacia = []

lista_vacia.append('Hola')
lista_vacia.append('Mundo')
lista_vacia.append('Python')

print(lista_vacia)

#ACTIVIDAD 4:
animales = ['perro', 'gato', 'conejo', 'pez'] 
animales[1] = 'loro'
animales[-1] = 'oso'

print(animales)

#ACTIVIDAD 5:
#El programa mostrado en el documento elimina el numero más grande de la lista.

#ACTIVIDAD 6:
diez_treinta = list(range(10, 31, 5))
print(diez_treinta[0:2])

#ACTIVIDAD 7:
autos = ['sedan', 'polo', 'suran', 'gol']
autos[1] = 'bronco'
autos[2] = 'virtus'

#ACTIVIDAD 8:
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)

print(dobles)

#ACTIVIDAD 9:
compras = [['pan', 'leche'], ['arroz', 'fideos', 'salsa'], ['agua']] 
# a) Agregar "jugo" a la lista del tercer cliente usando append. 
compras[2].append('jugo')
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
compras[1][1] = 'tallarines'
# c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove('pan')
# d) Imprimir la lista resultante por pantalla 
print(compras)

#ACTIVIDAD 10:
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)