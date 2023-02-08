#Jeremy Arthur Martinez Valoy (Matricula:21-1474)
#Realice un programa que replique la impresion de una factura, como la que se muestra a continuacion:

#Indicaciones:

'''Omitir las categorias de productos.
Capturar nombre del cliente y mostrarlo al inicio de la factura.
A diferencia de como se muestra en la imagen, INCLUIR una columna para la CANTIDAD del producto.
Hay productos que no llevan ITBIS, por lo que el programa debe de controlar esto, de modo que en la columna de ITBIS se tenga 0.00 si el producto no lleva, o el valor correspondiente si lleva.
Formula para el calculo del ITBIS: (precio / 1.18) * 0.18.
Los valores deben presentarse con 2 posiciones decimales (tal como en la imagen).
Se debe evitar capturar data basura.'''

#Se inicia el programa pidiendo al usuario que ingrese su nombre para que este sea mostrado en la factura. 
print("Ingrese el nombre a mostrar en la factura:")
nombre=input()
print ("FACTURA")
print("Cliente:", nombre)

print("===========================================")
print("=====FACTURA PARA EL CONSUMIDOR FINAL====== ")
print("===========================================")

#Se crea una lista que servira para almacenar los articulos introducidos por teclados. 
Lista=[]
total=0

#Se usa la condicion (while) para asignar las variables y las funciones que el programa va a ejecutar. 
while True: 
    
    #Se le dice al programa que los valores de las variables seran introducidos de forma dinamica (por teclado).
    producto= input("Ingrese el producto a facturar:")
    cantidad= int(input("Indica al cantidad del producto:"))
    precio= float(input("Indique el precio del producto:"))

    #Se usa (round) para que al final el valor decimal quede con solo dos numeros despues del punto. 
    subtotal=round(cantidad * precio, 2)
    total+=subtotal
    ITBIS= (round(precio / 1.18) * 0.18)
    SI=(subtotal+ITBIS)
    round(SI),2
    #Para que los valores se agreguen a la factura usamos (.append) y luego se le indica al programa como apareceran los datos. 
    Lista.append(("ARTICULO:" +producto+" -----> CANTIDAD x "+str(cantidad)+"  -----> PRECIO:"+str(precio)+"-----> ITBIS:"+str(round(ITBIS,2))+" RD$ -----> SUBTOTAL: " +str(round(SI,2))+ "RD$"))

    #Por ultimo se crea un pequeño menu para que el usuario elija entre continuar o terminar con la ejecucion del programa.     
    Fun=input("Para TERMINAR presione(X), para CONTINUAR presione (C)")
    if Fun == "X":
        print("===========================================")
        print("=====FACTURA PARA EL CONSUMIDOR FINAL====== ")
        print("===========================================")
        [print(p) for p in Lista]
        print("TOTAL:", round(subtotal,2),"RD$")
        break
    if Fun == "C":
        continue  

