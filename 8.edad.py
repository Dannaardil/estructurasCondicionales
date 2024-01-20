from time import localtime
t= localtime()

diaActual= t.tm_mday

mesActual= t.tm_mon

añoActual = t.tm_year

print ("ingrese su fecha de nacimiento->")

dia = int(input("Dia:  "))
mes = int(input("mes:  "))
año = int(input("año:  "))

edad = añoActual - año

if mesActual< mes or (mesActual == mes and diaActual < dia):
    edad -= 1
print(f"usted tiene {edad} años ")

