any = int(input("Introdueix un any: "))

digit1 = int(any/1000)
any = int(any%1000)

digit2 = int(any/100)
any = int(any%100)

digit3 = int(any/10)
any = int(any%10)

digit4 = any

print("Digit 1: {}  Digit 2: {}  Digit 3: {}  Digit 4: {}".format(digit1,digit2,digit3,digit4))