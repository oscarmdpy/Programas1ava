print("""
      1)Km
      2)mm
      3)mt""")
seleccion = int(input("ESculñ una opcio"))

if seleccion == 1:
  km = int(input("Quin valor?"))
  print("""
      1)mm
      2)mt""")

  conversion = int(input("en que vols convertirlo?"))
  if conversion == 1:
    print((km * 1000)/1852)
  elif conversion == 2:
    print((km * 1000)/1609)

  conversion = int(input("en que vols convertirlo?"))
  if conversion == 1:
    print((km * 1000)/1852)
  elif conversion == 2:
    print((km * 1000)/1609)
if seleccion == 2:
  mm = int(input("Quin valor?"))
  print("""
      1)km
      2)mt""")

  conversion = int(input("en que vols convertirlo?"))
  if conversion == 1:
    print(mm * 1852)
  elif conversion == 2:
    print((mm * 1,151))
if seleccion == 3:
  mt = int(input("Quin valor?"))
  print("""
      1)km
      2)mm""")
  conversion = int(input("en que vols convertirlo?"))
  if conversion == 1:
    print(mt * 1609)
  elif conversion == 2:
    print(mt / 1,151)
