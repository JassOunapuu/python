from random import randrange
import math

# Harjutus 04
# J. Õunapuu
# 03.02.2022


# Pank

konto = 0
intress = 0.05
raha = int(input("Sisestage rahasumma:  "))
konto += raha

aastad = int(input("Mitu aastat tahate raha hoiustada?: "))

print(f"{'aasta':4} {'Algsumma':10} {'Intress':10} {'Aasta lõpuks':10}  ")

for i in range(aastad):
    boonus = konto * intress
    print(f"{i+1:4} {konto:10.2f} {boonus:10.2f} {konto+boonus:10.2f}")
    konto += boonus
print(f"Summa kokku: {konto:.2f}")







# Arvamismäng

for i in range(1,2):
    nr = (randrange(1,21))

nr = 5
loop = 1
kordade_arv = 0
 
print("Arva ära number 1-20")
 
while loop == 1:
    arva = int(input("Sisesta number: "))
    
    if arva == nr:
        kordade_arv += 1
        print("Hästi paned!")
        loop = 0
    elif kordade_arv >= 2:
        loop = 0
        if input("Kas soovid veel mängida?(J/E)") == "J":
            loop = 1
            kordade_arv = 0
        else:
            print("nägemist!")
    elif arva < nr:
        kordade_arv += 1
        print("Sinu pakutud arv on liiga väike")
   # elif arva > nr:
   #     kordade_arv += 1
   #     print('Sinu pakutud arv on liiga suur')
    
    else:
        kordade_arv += 1
        print("Sinu pakutud arv on liiga suur")
        



#viisikud

for i in range(1,101):
    if i%5 == 0:
        print(i)
        




# Korrutustabel

for i in range(1,11):
    a=5
    v=i*a
    print(f"{a} x {i} = {v}")

print()






# Paaris ja paaritu

for i in range(1,101):
    if i%2 == 0:
        print(f"{i} paaris")
    else:
        print(f"{i} paaritu")


# Loto

from random import randrange
for i in range(1,6):
    print(randrange(0,9),end="")
print()
print()


# Tärnid

for i in range(1,6):
    for j in range(1,6):
        print('* ', end='')
    print()
print()

for i in range(1,6):
    print("* "* i)
    
print(" ")
k = 6
for t in range(1,6):
    k = k - 1
    print("* "* k)
    


# Jalgpalli meeskonna valimine

sugu = input("Sisestage oma sugu(M/K/N):  ")

if sugu.lower() == "m":
    vanus = int(input("Sisestage vanus:  "))
    if vanus >= 16 and vanus <= 18:
        print("youre in")
    else:
        print("no luck, bye")
else:
    print ("Sa ei kuulu siia")




# müük

hind = int(input("Sisesta toote hind, et saada soodust: "))
if hind <= 10:
    print ("Toote allahindlus on 10%")
    ale = 0.1
else:
    print ("Toote allahindlus on 20%")
    ale = 0.2
summa = hind - hind * ale

print (f"maksmisele kulub {summa} eurot")



#Juubel
synd = input("Sisesta sünniaeg kujul dd.mm.yyyy: ")
p, k, a = synd.split(".")
vanus = 2022 - int(a)
if vanus%5 == 0:
    print("On juubel")
else:
    print("Ei ole juubel")




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
else:
    print("Risttahukas")









