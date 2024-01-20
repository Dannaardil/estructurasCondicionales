operando = int(input("ingrese el operando: "))
operador = str(input(" Ingrese el operador : "))
operando2 = int(input("ingrese el operando : "))

suma = operando + operando2
resta = operando - operando2
multiplicacion = operando * operando2
division = operando / operando2


if operador == ("+") :
    print(f"{operando} {operador} {operando2} = {suma}")
elif operador == ("-") :
    print(f"{operando} {operador} {operando2} = {resta}")
elif operador == ("*") :
    print(f"{operando} {operador} {operando2} = {multiplicacion}")
elif operador == ("/") :
    print(f"{operando} {operador} {operando2} = {division}")