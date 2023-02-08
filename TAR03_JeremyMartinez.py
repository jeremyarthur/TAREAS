#Jeremy Arthur Martinez Valoy (Matricula: 21-1474)
"""Escriba un programa que calcule el precio a pagar por el suministro de energia electrica. 
Se debe preguntar la cantidad de kwh consumidos y el tipo de instalacion: R para residencias, I para industrias y C para comercios. """

#Comenzamos definiendo las variables: Residencia, Comercio e Industria. 
R= "Residencia"
I = "Industria"
C= "Comercio"



'''En este caso la variable inst hace referencia la tipo de instalacion. Damos la instruccion para que el programa de la 
opcion para seleccionar entre Comercio, Residencia o Industria.'''

inst= str(input("Seleccione el tipo de instalacion: (R)para Residencia, (I)para Industria, y (C)para Comercio."))




#Por ultimo usamos las condicionales para dar los diferentes precios segun el consumo y el tipo de instalacion. 
if inst==R:
    CR= int(input("Introduzca la cantidad consumida para Residencias"))
    if CR <= 500:
        print("El precio Residencial a pagar es de: RD$550.00")
    elif CR > 500:
        print("El precio Residencial a pagar es de: RD$850.00 ") 

if inst==I:
    CI= int(input("Introduzca la cantidad consumida para Industrias"))
    if CI <= 5000:
        print("El precio Industrial a pagar es de: RD$3800.00")
    elif CI > 5000:
        print("El precio Industrail a pagar es de: RD$4200.00")

if inst==C:
    CC= int(input("Introduzca la cantidad consumida para Comercios"))
    if CC <=1000:
        print("El precio comercial a pagar es de:RD$1300.00")
    elif CC > 1000:
        print("El precio comercial a pagar es de:RD$2500.00")