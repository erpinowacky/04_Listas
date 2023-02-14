'''Escriba un programa Python para multiplicar todos los elementos de una lista.'''

cNum = 0
num = 0.0
listNum = []
mulList = 1

print('*****CREAR LISTA Y AGREGAR NÚMEROS A LA LISTA*****')
cNum = int(input('Digite cantidad de números en la lista: '))
for i in range(cNum):
    num = float(input('Digite los números que quiere guardar en la lista: '))
    listNum.append(num)

print('*****LISTA*****')
print(listNum)
print()

print('*****MULTIPLICACIÓN DE LOS NÚMEROS GUARDADOS EN LA LISTA*****')
for i in listNum:
    mulList *= i
    print(i)
print(f'Total: {mulList}')


