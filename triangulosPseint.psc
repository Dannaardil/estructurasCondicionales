Algoritmo triangulos
	Definir a, b, c Como Real
	Escribir 'ingrese a: '
	Leer a
	Escribir 'ingrese el lado b: '
	Leer b
	Escribir 'ingrese el lado c: '
	Leer c
	Si (a+b)>c Y (b+c)>a Y (c+a)>b Entonces
		Si a==b Y a==c Y c==b Entonces
			Escribir 'es un triangulo equilatero'
			Si a==b Y c<>a O b==c Y a<>b O c==a Y b<>a Entonces
				Escribir 'es un triangulo isoceles'
				Si a<>b Y a<>c Y c<>b Entonces
					Escribir 'el triangulo es escaleno'
				FinSi
			FinSi
		FinSi
	SiNo
		Escribir 'no es un triangulo valido'
	FinSi
FinAlgoritmo
