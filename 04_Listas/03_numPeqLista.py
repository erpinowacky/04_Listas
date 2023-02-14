'''Escriba un programa Python para obtener el número más pequeño de una lista.'''

cNum = 0
num = 0.0
listNum = []
mulList = 1
peq = 100

print('*****CREAR LISTA Y AGREGAR NÚMEROS A LA LISTA*****')
cNum = int(input('Digite cantidad de números en la lista: '))
while cNum:
    num = float(input('Digite los números que quiere guardar en la lista no mayor a 100: '))
    if num > 100:
        print('Número muy grande')
        continue
    else:
        listNum.append(num)
    cNum -= 1

print('*****LISTA*****')
print(listNum)
print()

print('*****NÚMERO MAS PEQUEÑO HALLADO CON FUNCIÓN*****')
print(min(listNum))
print()

print('*****NÚMERO MAS PEQUEÑO HALLADO SIN FUNCIÓN*****')
for i in listNum:
    if i <= peq:
        peq = i 
print(peq)
