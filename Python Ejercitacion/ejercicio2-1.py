capital = int(input("Ingrese el capital inicial: "))
interes = int(input("Ingrese la tasa de interes: "))
anios = int(input("Ingrese el numero de años: "))

Cn = (capital * (1 + interes/100) ** anios)

print (Cn)