#Jeremy Arthur Martinez Valoy (Matricula: 21-1474)
'''Escriba una funcion que reciba 2 listas de productos (de forma dinamica), 
y retorne un conjunto (Set) de los productos comunes en las mismas. 
En caso de que no hayan productos comunes, retornar: "No hay productos comunes en las listas"'''

#Se crean dos listas.
lista1=[]
lista2=[]


#Se imprime la primera lista y se usa "for" introducir los productos por teclado. 
print('LISTA 1')
for i in range (4):
    art= str(input("Ingrese un producto:"))
    lista1.append(art)
print()

#Se imprime la segunda lista y se usa "for" introducir los productos por teclado. 
print('LISTA 2')
for i in range(4):
    art2 = str(input("Ingrese un producto:"))
    lista2.append(art2)
print()


#Se imprimen las listas. 
print("LISTA 1:\n",lista1)
print()

print("LISTA 2:\n",lista2)
print()


#Se convierten las listas en sets. 
set1=set(lista1)
set2=set(lista2)


#Se crea la condicion para la interseccion de ambos sets.
if set1.intersection(set2):
    inter=set1.intersection(set2)
    print("Productos comunes:\n",inter)

#Por ultimo se usa un else si la condicion no se cumple. 
else:
    print("No hay productos comunes en las listas")