# Jass Õunapuu
#  17.02.2022
#    IT-21


# Ruumalad

import math

def kuRuumala(a):
    v=a**3
    return v

def keRuumala(a):
    v=(4*math.pi*a**3)/3
    return v

def koRuumala(a,h):
    v=(math.pi*a**2*h)/3
    return v

def siRuumala(r,h):
    v=math.pi*r**2*h
    return v


number=0
loop=0
while loop == 0:
    kujund = int(input("Vali kujund\n 1) Kuup\n 2) Kera\n 3) Koonus\n 4) Silinder\n 5) Lõpeta\n Sisesta soovitud number: "))

    if kujund==1:
        number = int(input("Valisid kuubi. Sisesta kuubi küljepikkus:  "))
        print(f"Kuubi ruumala on: {kuRuumala(number)}")
    
    elif kujund==2:
        number = int(input("Valisid kera. Sisesta kera raadius:  "))
        print(f"Kera ruumala on: {keRuumala(number)}")
    
    elif kujund==3:
        number = int(input("Valisid koonuse. Sisesta koonuse raadius:  "))
        number2 = int(input("Sisesta koonuse kõrgus:  "))
        print(f"Koonuse ruumala on: {koRuumala(number,number2)}")
    
    elif kujund==4:
        number = int(input("Valisid silindri. Sisesta silindri raadius:  "))
        number2 = int(input("Sisesta silindri kõrgus:  "))
        print(f"Silindri ruumala on: {siRuumala(number,number2)}")
    else:
        loop=1

print()



# Tervitamise funktsioon

nimi = "Stoopid"
keel = "EN"
def tervita(nimi,keel):
    'Inimese tervitamine'
    if keel == "EN":
        tervitus = (f"Hello {nimi}")
    elif keel == "ET":
        tervitus = (f"Tere {nimi}")
    else:
        tervitus = (f"Guten tag {nimi}")
    return tervitus
print(tervita(nimi,keel))





