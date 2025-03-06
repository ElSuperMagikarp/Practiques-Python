import random

numeroEntrat = int(input("Intenta endivinar el numero (1-6): "))
numeroAleatori = random.randint(1,6)

missatge = "El numero era {}"
if numeroAleatori == 1:
    print(missatge.format("u"))
elif numeroAleatori == 2:
    print(missatge.format("dos"))
elif numeroAleatori == 3:
    print(missatge.format("tres"))
elif numeroAleatori == 4:
    print(missatge.format("quatre"))
elif numeroAleatori == 5:
    print(missatge.format("cinc"))
elif numeroAleatori == 6:
    print(missatge.format("sis"))

if numeroEntrat == numeroAleatori:
    print("L'HAS ENDIVINAT!! BOOOOOF")
else:
    print("HAS PERDUT PRINGAAAAT")