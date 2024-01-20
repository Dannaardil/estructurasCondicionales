año = int(input("ingrese un año : "))
añodivisible = año % 4

añodivisible2 = año % 400
añodivisible3 = año%100
  
if año> 1582:        
     if añodivisible3 == 0 and añodivisible2 != 0 :
        print(f"{año} es bisiesto")
        if añodivisible == 0 :
                print(f"{año} es bisiesto")


else :
   print(f"{año} no es bisiesto")

#elif añodivisible3 ==0  :
    #print(f"{año}  no es bisiesto")

#elif añodivisible == 0 :
    # print(f"{año} es bisiesto")
# print(f"{año} no es bisiesto ")