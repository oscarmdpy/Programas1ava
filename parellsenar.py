import random
print("""
      0) Parell
      1) Senar
    """)
eleccion = int(input("escull: \n"))
usuari = int(input("nombre?: "))
ord = random.randint(0,10)
if (ord + usuari) % 2 == 0 and eleccion == 0  :
  print(" La suma es parella,", ord + usuari,", has guanyat")
if (ord + usuari) % 2 == 0 and eleccion == 1  :
  print(" La suma es parella,", ord + usuari,", has perdut")
if (ord + usuari) % 2 == 1 and eleccion == 0  :
  print(" La suma es senar,", ord + usuari,", has perdut")
if (ord + usuari) % 2 == 1 and eleccion == 1  :
  print(" La suma es senar,", ord + usuari,", has guanyat")