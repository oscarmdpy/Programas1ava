from math import sqrt
A = int(input("Nombre elevat a 2\n"))
B = int(input("Nombre elevat a 1\n"))
C = int(input("Terme independent\n"))
if ((B**2)-4*A*C) < 0:
	print("La rael dona negativa")
else:
	print("les solucions són")
	print((-B+sqrt(B**2-(4*A*C)))/(2*A))
	print((-B-sqrt(B**2-(4*A*C)))/(2*A))

