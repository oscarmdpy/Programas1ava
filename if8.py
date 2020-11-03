dia = int(input("Diquem el dia\n"))
mes = int(input("Diguem el mes\n"))
any = int(input("Diguem l'any\n"))
if dia>=1 and dia>=30:
	print("aquesta data es incorrecta,hi han mes de 30 dies")
elif mes>=1 and mes>=12:
	print("aquesta data es incorrecta, no hi han mes de 12 mesos")
elif any>=2020:
	print("encara no hem arribat a aquest any")
else:
	print(dia,"/",mes,"/",any,"es correcta")
