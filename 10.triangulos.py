a = float(input("ingrese el lado a: "))
b = float(input("ingrese el lado b: "))
c = float(input("ingrese el lado c: "))

if (a + b)> c and (b + c)> a and (c + a)> b :
    if a == b and c != a  or b == c and a != b or c == a and b != a:
        print(f"Es un triangulo iscoceles")
    elif a != c and  a != b and c != b : 
        print(f"el triangulo es escaleno")
   
else :
    print(f"no es un triangulo valido")


