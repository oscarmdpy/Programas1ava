import random
print("""
      0) Cara
      1) Creu
    """)
eleccion = int(input("quin vols\n"))
a = random.randint(0,1)
if eleccion == 0 and a == 0:
  print("A sortit cara, has guanyat")
if eleccion == 0 and a == 1:
  print("A sortit creu, has perdut")
if eleccion == 1 and a == 0:
  print("A sortit cara, has perdut")
if eleccion == 1 and a == 1:
  print("A sortit creu, has guanyat")




  