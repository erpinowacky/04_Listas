'''Escriba un programa Python para sumar todos los elementos de una lista'''

listNum = []
sumList = 0.0

print('*****CREAR LISTA Y AGREGAR NÚMEROS A LA LISTA*****')
cNum = int(input('Digite cantidad de números en la lista: '))
for i in range(cNum):
    num = float(input('Digite los números que quiere guardar en la lista: '))
    listNum.append(num)

print('*****LISTA*****')
print(listNum)
print()

print('*****SUMA DE LOS NÚMEROS GUARDADOS EN LA LISTA*****')
for i in listNum:
    sumList += i
    print(i)    
print(f'Total: {sumList}')


