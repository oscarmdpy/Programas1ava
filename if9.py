dia = int(input("Diquem el dia\n"))
mes = int(input("Diguem el mes\n"))
any = int(input("Diguem l'any\n"))
if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and dia <= 31:
	print("La data es correcta")
else:
	print("incorrecta")
