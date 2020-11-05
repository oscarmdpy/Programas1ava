preuor = int(input("Quin es el preu original\n"))
preupg = int(input("quin preu has pagat?\n"))
descompte = int(preuor-preupg)
if descompte !=0: 
	print("el descompte es de:",descompte,"€")
	print ("es un",100*preupg/preuor-100,"%")
