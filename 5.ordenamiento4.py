num1 = int(input("ingrese un numero : "))
num2 = int(input("ingrese otro numero: "))
num3 = int(input("ingrese otro numero: "))
num4 = int(input("ingrese otro numero: "))
    
if  num1>num2 :
    num1, num2 = num2, num1 
if num2 >num3 :
    num2, num3 = num3, num2
if num3> num4:
    num3,num4 = num4, num3 
if  num1>num2 :
    num1, num2 = num2, num1 
if num2 >num3 :
    num2, num3 = num3, num2
if num1 > num2 : 
    num1, num2 = num2, num1 


print(f"{num1} {num2} {num3} {num4}")

