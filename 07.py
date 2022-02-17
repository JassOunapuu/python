# Jass Õunapuu
#  17.02.2022
#    IT-21


# Ruumalad
kujund=1
number=5
def ruumala(kujund,number):
    kujund = int(input("Vali kujund\n 1) Kuup\n 2) Kera\n 3) Koonus\n 4) Silinder\n Sisesta soovitud kujundi number: "))
    if kujund==1:
        number = int(input("Valisid kuubi. Sisesta kuubi serva pikkus:  "))
        print(f"Kuubi ruumala on: {number*number*number}")
    elif kujund==2:
        number = int(input("Valisid kera. Sisesta kera raadius:  "))
        print(f"Kera ruumala on: {4*(number*(number*3.14))}")
        
    elif kujund==3:
        number = int(input("Valisid koonuse. Sisesta koonuse raadius:  "))
        print(f"Koonuse ruumala on: {4*(number*(number*3.14))}")
        
    else:
        
        arv = arv1 * arv2
    return ruumala(1,6)






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





