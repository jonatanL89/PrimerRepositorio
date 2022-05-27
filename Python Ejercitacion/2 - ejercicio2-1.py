#Ejercicio 2.1. Escribir un programa que le pregunte al usuario una cantidad de pesos, una tasa de interés y un número de años y muestre como resultado el monto final a obtener. La fórmula a utilizar es: Cn = C * (1 + x/100) ^ n Donde C es el capital inicial, x es la tasa de interés y n es el número de años a calcular.


capital = int(input("Ingrese el capital inicial: "))
interes = int(input("Ingrese la tasa de interes: "))
anios = int(input("Ingrese el numero de años: "))

Cn = (capital * (1 + interes/100) ** anios)

print (Cn)