palabra1 = str(input("ingrese la primera palabra: "))
palabra2 = str(input("ingrese la segunda palabra: "))

caracteresp1 = len(palabra1)
caracteresp2 = len(palabra2)

extra = caracteresp1 - caracteresp2
extra2 = caracteresp2 - caracteresp1
if caracteresp1> caracteresp2 :
    print(f"la palabra {palabra1} tiene {extra} letras mas que {palabra2}")
elif caracteresp2 > caracteresp1 :
    print(f"la palabra {palabra2} tiene {extra2} letras\nmás que {palabra1} ")
else :
    caracteresp1 == caracteresp2 
    print(f"las dos palabras tienen el mismo largo ")