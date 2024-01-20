num1 = int(input("ingrese un numero"))
num2 = int(input("ingrese otro numero"))
num3 = int(input("ingrese otro numero"))

if num1>num2 :
    num1,num2 = num2,num1
if num2>num3 :
    num2,num3 = num3,num2 
if num1>num2 :
    num1,num2= num2,num1
print(f"{num1,num2,num3}")







#if num1<=num2 and num2<=num3: #1
  #  print(f"{num1} {num2} {num3}")
#elif num1<=num3 and num3<=num2: #1
      #print(f"{num1} {num3} {num2}")
#elif num2<=num3 and num3<=num1:#2
   # print(f"{num2} {num3} {num1}")
#elif num2<=num3 and num1<=num3:#2
   # print(f"{num2} {num1} {num3}")    
#elif num3<=num2 and num2<=num1 :#3
   # print(f"{num3} {num2} {num1}")
#elif num3<=num2 and num1<=num2 : #3
    #print(f"{num3} {num1} {num2}")