#Probar si un número es negativo

numero = float(input("Ingrese un numero cualquiera: "))           #ingreso de dato
while(numero == 0):                                         #bucle para controlar que el numero sea diferente de 0
    print("El numero debe ser diferente de 0")
    numero = int(input("Ingrese el numero: "))               #ingreso nuevamente del numero

if numero >0:                                               #compara si el numero mayor a 0 para mostrar el mensaje
    print("El numero es positivo")      
else:
    print("El numero es negativo")