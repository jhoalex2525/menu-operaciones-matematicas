#   menu de opciones
import math


opcion = 1

print("Operaciones matematicas")
print("******")
print("0. salir")
print("1. encontrar multiplo de 2")
print("2. encontrar raiz cuadrada")
print("3. sumar +100")
print("4. elevar a la 2")
print("******")
while(opcion != 0):
    opcion = int(input("Bienvenido, digita una opcion: "))
    if(opcion == 1):
        numero = int(input("digite un numero: "))
        if(numero%2 == 0):
            print(f"el numero {numero} es multiplo de 2")
        else:
            print(f"el numero {numero} no es multiplo de 2")
    elif(opcion == 2):
        numero = int(input("digite un numero: "))        
        print(f"la raiz cuadrada de {numero} es {math.sqrt(numero)}")
    elif(opcion == 3):
        numero = int(input("digite un numero: "))
        print(f"el numero {numero} mas 100 es {numero + 100}")
    elif(opcion == 4):
        numero = int(input("digite un numero: "))
        print(f"el numero {numero} elevado a la 2 es {math.pow(numero,2)}")
    elif(opcion == 0):
        print("saliendo del ciclo")
        break        
    else:
        print("digita una opcion valida")
else:
    print("saliendo del ciclo")