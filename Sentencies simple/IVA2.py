preu = int(input("Quin es el preu del producte?\n"))
IVA = int(input("quin es el porcentatge de IVA?\n"))
print("l'IVA són:", IVA/100*preu,"€")
print("El preu total es:",IVA/100*preu+preu,"€")
