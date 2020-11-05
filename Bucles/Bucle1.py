import random
a = random.randint(1,10)
b = int(input("adivina el numero de l'1 al 10"))
while a != b:
  b=int(input("dona un altre numero"))
if a==b:
  print("correcte!")