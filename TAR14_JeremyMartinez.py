#Jeremy Arthur Martinez Valoy (Matricula:21-1474)

'''Escriba un programa que dado un texto con n palabras realice lo siguiente:
Determine cuántas palabras comienzan con consonantes.
Determine cuántas palabras comienzan con vocales.
Con los resultados anteriores, retorne un diccionario, 
en conjunto con cuáles palabras comienzan con lo anteriormente mencionado.
Retorne el texto capitalizado.'''

#Se captura la cadena por teclado.
texto = input("INGRESE UNA CADENA DE CARACTERES:")
print()

#Se divide la cadena en palabras.
div=texto.split()

#Se define la variable que contiene las vocales
vocales=("a","e","i","o","u")

#Se crea la condicion para extraer las palabras que empiezan por vocales y consonantes.
for i in div:
    if i.startswith(vocales):
        cuenta1=i.count(i)
        dic=(i)
        
    else:
        cuenta2=i.count(i)
        dic2=(i)

#Se crea el diccionario con los resultados.
dicf={"vocal":dic, "consonante":dic2, "Cantidad de consonantes":cuenta2, "cantidad de vocales":cuenta1}
print(dicf)