Algoritmo ordenamiento 
	definir num1,num2,num3 Como Entero
	escribir "ingrese el primer numero: "
	leer num1
	escribir "ingrese el segundo numero : "
	leer num2
	escribir "ingrese el tercer numero: "
	leer num3 
	si num1>num2 
		temp <- num1 
		num1 <- num2
		num2 <- temp
	
	 
	FinSi
	si num2 > num3
		temp <- num1
		num2 <- num3
		num3 <- temp
	FinSi
	
	si num1>num2 
		temp <- num1
		num1 <- num2
		num2 <- temp
	
	FinSi
 escribir num1 " " num2 " " num3 
	
	
FinAlgoritmo
