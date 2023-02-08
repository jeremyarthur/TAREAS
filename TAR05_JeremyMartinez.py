#Jeremy Arthur Martinez Valoy (Matricula 21-1474)
'''Escriba un programa que pregunte al usuario los numeros de su ticket de loteria, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor. '''


#Se muestra un mensaje de bienvenida
print("Lista de Numeros")

#Se crea un lista con un rango de 8 numeros que seran introducidos por teclado. 
lista=[]
for x in range (8):
    num=int(input("Ingrese sus numeros de loteria:"))
    lista.append(num)

#Finalmente con ".sort" el programa organiza los numeros de menor a mayor.
lista.sort()
print(lista)

