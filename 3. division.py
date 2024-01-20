dividendo = int(input("ingrese el dividendo: "))
divisor = int(input("ingrese el divisor: "))
division = dividendo % divisor
if division > 0 :
 print (f"la division no es exacta")
else :
    print(f"la division es exacta")