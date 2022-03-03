# pedir 20 numeros
contador = 1
sumatoria = 0
while(contador <= 5):
    numero = int(input("ingrese numero: "))
    if(numero < 0 ):
        sumatoria+=1
    contador+=1
print(f"hay {sumatoria} numeros negativos")