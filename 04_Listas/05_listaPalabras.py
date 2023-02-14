'''Escriba un programa Python para encontrar la lista de palabras que son más largas que n 
de una lista dada de palabras'''

cPal = 0
listPal = []
n = 0
nList = []

print('*****CREAR LISTA Y AGREGAR NÚMEROS A LA LISTA*****')
cPal = int(input('Digite cantidad de palabras en la lista: '))
for i in range(cPal):
    palabra = input('Digite las palabras que quiere guardar en la lista: ')
    listPal.append(palabra)

print('*****LISTA*****')
print(listPal)
print()

print('*****TAMAÑO DE LA PALABRA*****')
n = int(input('Digite el tamaño de la palabra: '))
for i in listPal:
    tamaño = len(i)
    if tamaño > n:
        nList.append(i)
print(nList)

