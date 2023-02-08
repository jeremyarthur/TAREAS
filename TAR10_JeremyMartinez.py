#Jeremy Arthur Martinez Valoy (Matricula: 21-1474)
'''Escriba un programa que, mediante el uso de funciones realice lo siguiente:
Dado un numero entero, realice la suma de sus digitos.
Con el resultado de la suma, realizar lo siguiente:
Generar los numeros del 1 al s (suma), y a su vez hacer las siguientes condiciones:
Si el numero es divisor de 3, mostrar el numero y la palabra "Fizz".
Si el numero es divisor de 5, mostrar el numero y la palabra "Buzz".
Si el numero es divisor de 3 y 5 (ambos), mostrar el numero y la palabra "FizzBuzz".
Si el numero no es divisor de ninguno (3 y 5), unicamente mostrar el numero.'''

#Funcion para sumar digitos.
def suma_de_digitos(n):
    suma = 0
    for g in str(n):
        suma+= int (g)
    return suma

#variable para ingresar de manera dinamica un numero entero.
n=int(input("Ingrese un numero entero:"))

#Se almacena la funcion en la variable (x).
x=suma_de_digitos(n)

#Se imprime el resultado de la suma de los digitos:
print('La suma de los digitos es:', x)
print()


#Se enlistan los numeros desde el 1 hasta s del resultado de la suma de los digitos.
j=range(1,x+1)
lista=list(j)
print(lista)
print()

#Se crean 4 listas.
nd=[]
fizzbuzz=[]
buzz=[]
fizz=[]

#Se crean las condiciones.
for i in lista:
    if i%3==0:
        fizz.append(i)
    
    if i%5==0:
        buzz.append(i)
    
    if i%3==0 and i%5==0:
        fizzbuzz.append(i)
    
    if i%3!=0 or i%5!=0:
        nd.append(i)


#Finalmente se imprimen los resultados.
print("====================\nFIZZ\n====================")
for i in fizz:
    print(i)
print()

print("====================\nBUZZ\n====================")
for i in buzz:
    print(i)
print()

print('====================\nFIZZBUZZ\n====================')
for i in fizzbuzz:
    print(i)
print()

print('====================\nNO DIVISIBLE\n====================')
for i in nd:
    print(i)
print()