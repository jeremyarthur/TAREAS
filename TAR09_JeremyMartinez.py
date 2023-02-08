#Jeremy Arthur Martinez Valoy (Matricula: 21-1474)
#Escriba un programa que, mediante una función, dada una cadena de caracteres (sin espacios), muestre el primer caracter que no se repite.


#Se define la funcion y se crea un diccionario
def pcnr(caracteres):
    contar = {}

    for c in caracteres:
        if c in contar:
            contar[c] += 1
        else:
            contar[c] = 1

#Use (.keys) que sirve para encontrar datos dentro del diccionario.     
    for c in contar.keys():
        if contar[c] == 1:
            return c

#Se define la variable que va a capturar los caracteres y luego, se le indica al programa que imprima el primer caracter que no se repite. 
oracion = str(input("Escriba una oracion:"))
print(f'El primer caracter que no se repite es:', {pcnr(oracion)})




