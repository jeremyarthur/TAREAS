#Jeremy Arthur Martinez Valoy (Matricula 21-1474)
'''Escriba un programa que permita crear una lista de palabras y que,
a continuacion, pida una palabra y diga cuantas veces aparece esa palabra en la lista'''



#Primero se le indica la programa imprima un mensaje de bienvenida para luego introducir por teclado los elementos de la lista. 
print("Bienvenido a su lista de compras")
lista=[]



#Se le indica al programa que a la lista se le introducira 8 elementos por teclado.
#Para esto se usa el comando "range". Y para que los elementos se agreguen se usa ".append".
for i in range(8):
    art=str(input("Ingrese un articulo para agregar a la lista:"))
    lista.append(art)



#Se crea un menu para seleccionar entre buscar o contar elementos de la lista.
acc= str(input('Seleccione que accion ejecutar, (1) para buscar en la lista o (2) para contar un articulo:'))




#Se usan condicionales para las opciones seleccionadas



'''En el caso de haber seleccionado buscar un elemento, se ingresa el elemento a buscar y luego el programa dice si el elemento
Esta o no en a lista'''
if acc == "1":
    Artc= str(input("Ingrese el articulo que desea buscar:"))   
    if Artc not in lista:
        print((Artc),"No esta en la lista")
    elif Artc in lista:
        print(Artc, "Esta en la lista")   





'''En el caso de haber seleccionado contar un elemento, se ingresa el elemento que se va a contar y luego
el programa dice la cantidad de veces que dicho elemento se repite'''
if acc== "2":
    Prd=str(input("Ingrese el producto que quiere contar:"))
    veces= lista.count(Prd)
    if Prd in lista: 
        print("El articulo se repite", veces, "veces") 
    elif Prd not in lista:
        print(Prd, 'no esta en la lista')













