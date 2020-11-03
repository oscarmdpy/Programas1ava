dia = int(input("Diquem el dia\n"))
mes = int(input("Diguem el mes\n"))
any = int(input("Diguem l'any\n"))
if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and dia>=1 and dia <= 31:
	print("La data es correcta")
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia>=1 and dia <=30:
  print("La data es correcta")
elif any % 4 == 0 and any % 100 != 0 or any % 400 == 0 and mes == 2:
  if dia >=1 and dia <=29:
    print("la data es correcta")
  else:
    print("La data es incorrecta")
elif any % 4 != 0 and any % 100 != 0 or any % 400 != 0 and mes == 2:
  if dia <= 28:
    print("La data es correcta")
  else:
    print("La data es incorrecta")
else:
  print("La data es incorrecta")
