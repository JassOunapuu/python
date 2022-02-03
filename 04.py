# Harjutus 04
# J. Õunapuu
# 03.02.2022


#juubel
sunna = input("Sisesta oma sünnipäev:  ")
paev,kuu,aasta = sunna.split(".")




#matemaatika
arv1 = int(input("Sisesta arv 1:  "))
arv2 = int(input("Sisesta arv 2:  "))
tehe = int(input("vali tehe:\n 1) liitmine\n 2) lahutamine\n 3) korrutamine\n 4) jagamine"))

if tehe==1:
    arv = arv1 + arv2
elif tehe==2:
    arv = arv1 - arv2
elif tehe==3:
    arv = arv1 / arv2
else:
    arv = arv1 * arv2

print(arv)

#Ruudu kontroll == > < >= >= !=
a = int(input("Sisesta ruudu üks külg:  "))
b = int(input("Sisesta ruudu teine külg:  "))
if a == b:
    print("Tegemist on ruuduga")
#elif:
#    klsdjlaj
else:
    print("Risttahukas")







