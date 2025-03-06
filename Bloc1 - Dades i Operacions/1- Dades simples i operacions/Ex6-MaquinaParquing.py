horaEntrada = int(input("Introdueix l'hora d'entrada: "))
minutsEntrada = int(input("Introdueix els minuts d'entrada: "))
horaSortida = int(input("Introdueix l'hora de sortida: "))
minutsSortida = int(input("Introdueix els minuts de sortida: "))

tempsEntrada = minutsEntrada + horaEntrada*60
tempsSortida = minutsSortida + horaSortida*60

diferenciaTemps = tempsSortida-tempsEntrada
preuCentims = int(diferenciaTemps/3)
preuEuros = preuCentims/100

print("El preu total és: "+str(preuEuros)+"€")