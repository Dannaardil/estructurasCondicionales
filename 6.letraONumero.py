primero = (input("ingrese caracter: "))
if primero.isupper():
    print(f"{primero} es una mayuscula")
elif primero.isalpha():
    print(f"{primero} es una letra")
elif primero.isnumeric():
    print(f"{primero} es un caracter")
else: 
    print(f"{primero} no es ni una letra ni un caracter ")