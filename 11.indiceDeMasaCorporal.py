estatura = float(input("Ingrese su estatura: "))
peso = float(input("ingrese su peso: "))
edad = int(input("ingrese su edad: "))


imc = peso/ estatura**2

if edad< 45:
    if imc<22.0:
        print("Tiene bajo riesgo de sufrir enfermedades coronarias")
    if imc>=22.0 :
        print(" tiene riego medio de sufrir enfermedades coronarias")
if edad>= 45 :
    if imc < 22.0:
        print("tiene riesgo medio de sufrir enfermedades coronarias")
    if imc >= 22.0:
        print("tiene riesgo alto de sufrir enfermedades coronarias")
         
 
    
