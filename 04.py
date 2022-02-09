# Harjutus 04
# J. Õunapuu
# 03.02.2022


# Arvamismäng






'''
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
    
'''

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









