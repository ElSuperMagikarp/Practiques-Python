notaPractiques = int(input("Introdueix la nota de les pràctiques: "))
notaTeoria = int(input("Introdueix la nota de la teoria: "))

PES_PRACTIQUES = 70
PES_TEORIA = 30

if notaPractiques < 3:
    notaPractiques = 0
if notaTeoria < 3:
    notaTeoria = 0

print("Mitjana:",mitjana := notaPractiques*PES_PRACTIQUES/100 + notaTeoria*PES_TEORIA/100)

if mitjana == 10:
    print("Matricula d'honor")
elif mitjana >= 9:
    print("Excel·lent")
elif mitjana >= 7:
    print("Notable")
elif mitjana >= 5:
    print("Aprovat")
elif mitjana >= 0:
    print("womp womp")
else:
    print("bro que putes has fet")