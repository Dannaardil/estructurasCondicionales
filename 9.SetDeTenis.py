a = int(input("cuantos juegos ha ganado el jugador a: ")) 
b =int(input("cuantos juegos ha ganado el jugador b: "))

if(a == 4 and b == 5):
    print("aun no termina")
elif(a >= 5 and b == 7):
    print("el jugador b gano el set")
elif(a == 5 and b == 6):
    print("aun no termina")
elif (a == 3 and b == 7):
    print("resultado invalido" )
elif(a <= 6 and b <= 4):
    print("el jugador a gano el set")
    