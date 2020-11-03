dia = int(input("Diquem el dia\n"))
mes = int(input("Diguem el mes\n"))
any = int(input("Diguem l'any\n"))
hora = int(input("Diguem l'hora\n"))
minuts = int(input("Diguem els minuts\n"))
segons = int(input("Diguem els segons\n"))
if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and dia>=1 and dia <= 31:
  if segons == 59 and minuts >0 and minuts <= 58 and hora >0 and hora <= 24: 
	  print(dia, mes, any, hora, minuts +1, segons * 0)
  elif segons >=1 and segons <=58 and minuts >0 and minuts <= 59 and hora >0 and hora <= 24:
    print(dia, mes, any, hora, minuts, segons + 1)
  elif segons == 59 and minuts == 59 and hora >0 and hora <= 22:
    print(dia, mes, any,hora +1,  minuts * 0, segons * 0)
  elif segons == 59 and minuts == 59 and hora == 23 and dia <= 30:
    print(dia + 1, mes, any,hora *0,  minuts * 0, segons * 0)
  elif segons == 59 and minuts == 59 and hora == 23 and dia == 31 and mes <= 11:
    print(dia -30, mes +1, any, hora*0, minuts *0, segons *0)
  elif segons == 59 and minuts == 59 and hora == 23 and dia == 31 and mes == 12:
    print(dia -30, mes -11, any +1, hora*0, minuts *0, segons *0)
  else:
    print("La data es incorrecta")

elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia>=1 and dia <=30:
  if segons == 59 and minuts >0 and minuts <= 58 and hora >0 and hora <= 24: 
	  print(dia, mes, any, hora, minuts +1, segons * 0)
  elif segons >=1 and segons <=58 and minuts >0 and minuts <= 59 and hora >0 and hora <= 24:
    print(dia, mes, any, hora, minuts, segons + 1)
  elif segons == 59 and minuts == 59 and hora >0 and hora <= 22:
    print(dia, mes, any,hora +1,  minuts * 0, segons * 0)
  elif segons == 59 and minuts == 59 and hora == 23 and dia <= 29:
    print(dia + 1, mes, any,hora *0,  minuts * 0, segons * 0)
  elif segons == 59 and minuts == 59 and hora == 23 and dia == 30 and mes <= 11:
    print(dia -29, mes +1, any, hora*0, minuts *0, segons *0)
  else:
    print("La data es incorrecta")

  

elif any % 4 == 0 and any % 100 != 0 or any % 400 == 0 and mes == 2:
  if dia >=1 and dia <=29:
    if segons == 59 and minuts >0 and minuts <= 58 and hora >0 and hora <= 24: 
	    print(dia, mes, any, hora, minuts +1, segons * 0)
    elif segons >=1 and segons <=58 and minuts >0 and minuts <= 59 and hora >0 and hora <= 24:
      print(dia, mes, any, hora, minuts, segons + 1)
    elif segons == 59 and minuts == 59 and hora >0 and hora <= 22:
      print(dia, mes, any,hora +1,  minuts * 0, segons * 0)
    elif segons == 59 and minuts == 59 and hora == 23 and dia <= 28:
      print(dia + 1, mes, any,hora *0,  minuts * 0, segons * 0)
    elif segons == 59 and minuts == 59 and hora == 23 and dia == 29 and mes <= 11:
      print(dia -28, mes +1, any, hora*0, minuts *0, segons *0)
    else:
      print("La data es incorrecta")
  else:
    print("La data es incorrecta")


elif any % 4 != 0 and any % 100 != 0 or any % 400 != 0 and mes == 2:
  if dia <= 28:
    if segons == 59 and minuts >0 and minuts <= 58 and hora >0 and hora <= 24: 
	    print(dia, mes, any, hora, minuts +1, segons * 0)
    elif segons >=1 and segons <=58 and minuts >0 and minuts <= 59 and hora >0 and hora <= 24:
      print(dia, mes, any, hora, minuts, segons + 1)
    elif segons == 59 and minuts == 59 and hora >0 and hora <= 22:
      print(dia, mes, any,hora +1,  minuts * 0, segons * 0)
    elif segons == 59 and minuts == 59 and hora == 23 and dia <= 27:
      print(dia + 1, mes, any,hora *0,  minuts * 0, segons * 0)
    elif segons == 59 and minuts == 59 and hora == 23 and dia == 28 and mes <= 11:
      print(dia -27, mes +1, any, hora*0, minuts *0, segons *0)
    else:
      print("La data es incorrecta")
  else:
    print("La data es incorrecta")
else:
  print("La data es incorrecta")
