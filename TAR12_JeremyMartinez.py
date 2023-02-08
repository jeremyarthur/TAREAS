#Jeremy Arthur Martinez Valoy (Matricula:21-1474)
'''Escriba un programa con funciones definidas por usted, que realice lo siguiente:
Almacene una lista de 10 tuplas que correspondan a los siguientes viajeros de un aeropuerto. 
Nota: La estructura de los datos de cada viajero es Nombre, Edad, Destino:
Juan, 30, Madrid.
Fernanda, 42, Portugal.
Raúl, 28, Brazil.
Julio, 32, Venezuela.
Mateo, 26, Argentina.
María, 32, Portugal.
José, 29, Madrid.
Marcos, 29, Venezuela.
Juana, 41, Venezuela.
Paulina, 35, Madrid.
Muestre los destinos almacenados (sin repetir).
Devuelva una lista de diccionarios de los pasajeros cuyo destino sea el solicitado por teclado.
Si se coloca un destino que no se encuentra en los almacenados, el programa debe mostrar un mensaje diciendo: 
"No hay pasajeros para este destino".'''

#Se crea una lista con las tuplas que continen los datos de los viajeros.
viajeros=[
        ('Juan', 30, 'Madrid'),
        ('Fernanda', 42, 'Portugal'),
        ('Raúl', 28, 'Brazil'),
        ('Julio', 32, 'Venezuela'),
        ('Mateo', 26, 'Argentina'),
        ('María', 32, 'Portugal'),
        ('José', 29, 'Madrid'),
        ('Marcos', 29, 'Venezuela'),
        ('Juana', 41, 'Venezuela'),
        ('Paulina', 35, 'Madrid')
        ] 


#Se crea una lista para los destinos, la cual, se pasara a set (para imprimir los destinos almacenados sin repetir).
destinos=[]
for i in viajeros:
        #Se sacan los destinos de las tuplas
        destinos.append(i[2])
        x=set(destinos)

#Se imprimen los destinos sin repetir.
print()
print("========\nDESTINOS\n========\n",x)
print()

#Se crea una lista para los pasajeros y las edades.
pasajeros=[]
for i in viajeros:
        pasajeros.append(i[0])

edades=[]
for i in viajeros:
        edades.append(i[1])


#Se crean los diccionarios a partir de los datos extraidos. 
pas1={"Nombre":pasajeros[0], "Edad":edades[0], "Destino":destinos[0]}
pas2={"Nombre":pasajeros[1], "Edad":edades[1], "Destino":destinos[1]}
pas3={"Nombre":pasajeros[2], "Edad":edades[2], "Destino":destinos[2]}
pas4={"Nombre":pasajeros[3], 'Edad':edades[3], 'Destino':destinos[3]}
pas5={"Nombre":pasajeros[4], 'Edad':edades[4], 'Destino':destinos[4]}
pas6={"Nombre":pasajeros[5], 'Edad':edades[5], 'Destino':destinos[5]}
pas7={"Nombre":pasajeros[6], 'Edad':edades[6], 'Destino':destinos[6]}
pas8={"Nombre":pasajeros[7], 'Edad':edades[7], 'Destino':destinos[7]}
pas9={"Nombre":pasajeros[8], 'Edad':edades[8], 'Destino':destinos[8]}
pas10={"Nombre":pasajeros[9], 'Edad':edades[9], 'Destino':destinos[9]}


#Se crea una funcion para hacer la impresion de los diccionarios, segun el usuario escriba el destino a buscar. 
def viajeros():        
        print('OJO; FAVOR ESCRIBA LA PRIMERA LETRA DEL DESTINO EN MAYUSCULAS.')
        z=input("Buscar pasajeros con destino a:")

        if z == "Madrid":
                print(pas1) 
                print(pas7) 
                print(pas10)
        
        elif z == "Portugal":
                print(pas2)
                print(pas6)

        elif z == "Brazil":
                print(pas3)

        elif z == "Venezuela":
                print(pas4)
                print(pas8) 
                print(pas9)

        elif z== "Argentina":
                print(pas5)

        else:
                print("No hay pasajeros para este destino")

#Finalmente se llama la funcion
viajeros()
