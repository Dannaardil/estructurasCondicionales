Algoritmo ordenamiento4
	definir num1, num2, num3, num4 Como Entero
	escribir "ingrese el primer numero: "
	leer num1
	escribir "ingrese el segundo numero: "
	Leer num2
	escribir "ingrese el tercer numero: "
	leer num3
	
	escribir "ingrese el cuarto numero: "
	leer num4
	
	
	si num1>num2
		temp <- num1
		num1<- num2
		num2 <- temp
	FinSi
	si num2>num3 
		temp <- num2 
		num2 <- num3 
		num3 <- temp
	FinSi
	
	si num3>num4
		temp <- num2
		num2<- num3 
		num3<- temp
	FinSi
	si num1>num2
		Temp <- num3 
		num3 <- num4
		num4 <- temp
	FinSi
	si num2>num3 
		temp <- num2 
		num2 <- num3 
		num3 <- temp
	FinSi
	si num1>num2
		Temp <- num3 
		num3 <- num4
		num4 <- temp
	FinSi
	
	escribir num1," ", num2," ", num3, " ",num4
	
FinAlgoritmo
