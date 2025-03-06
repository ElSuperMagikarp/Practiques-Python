numero = int(input("Introdueix un numero de fins 3 xifres: "))

if int(numero/1000) > 0:
    print("ERROR: El nombre té més de 3 xifres")
elif int(numero/100) > 0:
    #NUMERO TÉ 3 XIFRES
    digit1 = int(numero/100)
    numero = int(numero%100)
    digit3 = int(numero%10)
    if digit1 == digit3:
        print("És cap i cua")
    else:
        print("No és cap i cua")
elif int(numero/10) > 0:
    #NUMERO TÉ 2 XIFRES
    digit1 = int(numero/10)
    digit2 = int(numero%10)
    if digit1 == digit2:
        print("És cap i cua")
    else:
        print("No és cap i cua")
else:
    print("És cap i cua")