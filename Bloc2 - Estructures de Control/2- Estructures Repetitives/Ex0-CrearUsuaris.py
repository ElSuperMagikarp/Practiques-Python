quantUsuaris = int(input("Quans usuaris vols crear? "))

for i in range(1,quantUsuaris+1):
    nomUsuari = "user{}".format(i)

    print("useradd -m -s /bin/bash {}".format(nomUsuari))
    print("echo \"{}:{}\" | chpasswd".format(nomUsuari,"patata"))
    print("cd /home/{}".format(nomUsuari))
    print("mkdir src")
    print("mkdir tests")
    print("mkdir docs")
    print()
    print()
