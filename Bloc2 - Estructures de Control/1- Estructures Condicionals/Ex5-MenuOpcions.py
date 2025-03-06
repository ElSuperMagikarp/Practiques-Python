print("O P C I O N S")
print()
print("1. Escriure “Iniciar servidor web”")
print("2. Escriure “Iniciar servidor d’arxius”")
print("3. Verificar servei")
print()

eleccio = int(input("Escull una opció: "))

if eleccio == 1:
    print("Iniciar servidor web")
elif eleccio == 2:
    print("Iniciar servidor d’arxius")
elif eleccio == 3:
    lletraEleccio = input("Vols escriure “Iniciar servidor web”(W) o “Iniciar servidor d’arxius”(A)? ")
    if lletraEleccio == 'W':
        print("Iniciar servidor web")
    elif lletraEleccio == 'A':
        print("Iniciar servidor d’arxius")