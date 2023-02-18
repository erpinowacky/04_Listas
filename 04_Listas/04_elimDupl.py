'''Escriba un programa Python para eliminar duplicados de una lista.'''

cNum = 0
num = 0.0
listNum = []
contador = 0

print('*****CREAR LISTA Y AGREGAR NÚMEROS A LA LISTA*****')
cNum = int(input('Digite cantidad de números en la lista: '))
for i in range(cNum):
    num = float(input('Digite los números que quiere guardar en la lista: '))
    listNum.append(num)

print('*****LISTA*****')
print(listNum)
print()

print('*****ELIMINAR DUPLICADO DE LA LISTA*****')
for i in listNum:
    contador = listNum.count(i)
    if contador > 1:
        listNum.remove(i)
print(listNum)

