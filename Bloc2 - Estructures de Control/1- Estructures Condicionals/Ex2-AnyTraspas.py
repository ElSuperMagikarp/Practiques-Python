any = int(input("Introdueix un any: "))

if int(any%400) == 0:
    print("L'any és de transpás")
elif int(any%100) == 0:
    print("L'any NO és de transpás")
elif int(any%4) == 0:
    print("L'any és de transpás")
else:
    print("L'any NO és de transpás")