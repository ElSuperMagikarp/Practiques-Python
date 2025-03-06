hores = int(input("Entra una quantitat d'hores: "))
minuts = int(input("Entra una quantitat de minuts: "))
segons = int(input("Entra una quantitat de segons: "))

sumaSegons = segons + minuts*60 + hores*3600

print("L'equivalent en segons és: "+str(sumaSegons)+"s")

segons = int(input("Entra una quantitat de segons: "))

hores = int(segons/3600)
segons = int(segons%3600)
minuts = int(segons/60)
segons = int(segons%60)

print("L'equivalent en hores, minuts, i segons és: {}h {}m {}s".format(hores,minuts,segons))