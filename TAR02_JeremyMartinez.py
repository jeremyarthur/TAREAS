#Jeremy Arthur Martinez Valoy (Matricula:21-1474)
#Escribir un programa que pida 2 numeros y muestre paso a paso el calculo de la raiz cuadrada de la suma del cuadrado de ambos. 


"""Lo primero que se hace es indicarle al programa las variables que se van a introducir
por teclado, en este caso, son numeros tanto enteros como decimales, por lo tantos se escribe (float)."""

num1= float(input("Introduzca el primer valor:"))
num2= float(input("Introduzca el segundo valor:"))

"""Ahora se les asignan operaciones matematicas a las variable exp1, exp2 y sum."""

exp1= num1**2
exp2= num2**2
sum= (exp1+exp2)

"""Usamos (import math) para ingresar la instruccion (math.sqrt), que se usa para
sacar la raiz cuadrada de un valor, en este caso el resultado de la variable (sum)."""

import math
resultado= (math.sqrt(sum))



"""Con el comando "print" le indicamos al programa que mensaje mostrar luego de introducir los datos
y que se generen los resultados para las variables."""

print ("√","(","a^2 + b^2",")")
print("a=",num1,"b=",num2)
print("√","(",num1,"^2","+",num2,"^2"")", ) 
print("√","(",exp1,"+",exp2,")")
print("√","(",sum,")") 
print(resultado)


