nombre1 = int(input("donam un numero\n"))
nombre2 = int(input("donam un altre numero\n"))
resultat = int(nombre1*nombre2)
if resultat > 0:
	print("el seu producte es major a 0")
elif resultat < 0:
	print("el seu producte es menor a 0")
else:
	print("el seu producte es igual a 0")
