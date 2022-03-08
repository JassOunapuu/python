#  Jass Õunapuu
#      IT21
#   08.03.2022
import math



# 4.6

def kuu_nimi(a):
    kuud = ["","jaan","veeb","mär","apr"]
    return kuud[a]
print(kuu_nimi(1))

def kuupaev_sonena(b):
    dd,mm,yy = b.split(". ")
    print(dd,kuu_nimi(mm),yy)
    
kuupaev_sonena("6.9.1969")
    
# 4.5

def pronksikarvad(a):
    summa = 0
    fail = open(a, encoding="UTF-8")
    for i in fail:
        if (i) < 6:
            summa += i
    return summa
print("hoiupörsasse läheb",pronksikarvad("mundid.txt"))


# 4.4

kulalised = int(input("Mitu külalist tuleb?:  "))
def tervitus(a):
    for i in range(a):
        print('Võõrustaja: "Tere!"')
        print(f"Täna on {i+1}. kord tervitada, mõtiskleb võõrustaja")
        print('Külaline: "Tere, suur tänu kutse eest!"')
tervitus(kulalised)

# 4.3

def eelarve(a):
    summa = 55 + (10 * a)
    return summa
kuts = int(input("Mitu inimest on kutsutud? :  "))
tuleb = int(input("Mitu inimest tuleb? :  "))


print("Maksimaalne eelarve:",eelarve(kuts),"€")
print("Maksimaalne eelarve:",eelarve(tuleb),"€")


# 4.2

def mahlapakkide_arv(kogus):
    mahlapakkidearv = round(kogus*0.4/3,0)
    return mahlapakkidearv
kg = int(input("Sisesta õunte kogus:  "))
print(mahlapakkide_arv(kg))



# 4.1

kuva = int(input("Mitu korda soovid kuvada:  "))
def banner(t,k):
    for i in range(k):
        print(t.upper())

banner("Osta ja Sa ei kahetse!", kuva)
print()









# 3.5

fail = open("nimekiri.txt", encoding="UTF-8")
from datetime import *
kp = datetime.now().day
for i in fail:
    print(i)

# 3.4
lugu = 1
fail1 = input("Sisestage failinimi:  ")
fail = open(fail1, encoding="UTF-8")
number = 1
for i in fail:
    print(str(number)+". " +str(i), end=" ")
    number += 1    

print()

laul = int(input("Mis lugu tahad:  "))
for i in fail:
    if lugu == laul:
        print(i)
    lugu += 1

