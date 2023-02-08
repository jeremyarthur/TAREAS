#Jeremy Arthur Martinez Valoy (Matricula: 21-1474)
#Escriba un programa que, mediante el uso de funciones, retorne las tablas de multiplicar del n al m


#Se definen las variables. 
n =int(input("Ingrese el número por el que comenzarán a mostrarse las tablas:")) 
m =int(input("Ingrese el número por el que terminarán a mostrarse las tablas:"))
desde = 1 
hasta = 12


#Se crea la funcion que se va a ejecutar, en este caso "mult" que seria para multiplicar.
def mult(n,m):
    return(n*m)

#Se usa "for" para determinar el rango de las tablas y tambien para imprimir la operacion al final 
for i in range(n, m + 1):
    print(f'============================= \n Tabla de multiplicar del {i}:\n=============================') 
    for j in range(desde, hasta + 1):
        print(f'{i} x {j} = {i*j}')

#Este print se usa para dejar una linea en blanco entre cada tabla.
print() 

