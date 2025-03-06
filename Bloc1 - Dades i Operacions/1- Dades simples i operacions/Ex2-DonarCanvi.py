dinersIntroduits = float(input("Introdueix una quantitat de diners: "))
print()

euros2 = int(dinersIntroduits/2)
dinersIntroduits = dinersIntroduits%2

euros1 = int(dinersIntroduits/1)
dinersIntroduits = dinersIntroduits%1

centims50 = int(dinersIntroduits/0.5)
dinersIntroduits = dinersIntroduits%0.5

centims20 = int(dinersIntroduits/0.2)
dinersIntroduits = dinersIntroduits%0.2

centims10 = int(dinersIntroduits/0.1)
dinersIntroduits = dinersIntroduits%0.1

centims05 = int(dinersIntroduits/0.05)
dinersIntroduits = dinersIntroduits%0.05

centims02 = int(dinersIntroduits/0.02)
dinersIntroduits = dinersIntroduits%0.02

centims01 = int(dinersIntroduits)

print("Monedes de 2€:",euros2)
print("Monedes de 1€:",euros1)
print("Monedes de 50c:",centims50)
print("Monedes de 20c:",centims20)
print("Monedes de 10c:",centims10)
print("Monedes de 5c:",centims05)
print("Monedes de 2c:",centims02)
print("Monedes de 1c:",centims01)