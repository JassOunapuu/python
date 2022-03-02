#  Jass Õunapuu
#   02.03.2022
#     IT21
import math
#kolmnurga ümbermõõt
a = 2
b = 3
c = 4

P = a+b+c
print(f"Komnurga ümbermõõt on {P} cm")

#toote hind
hind = 36.75
hind2 = hind * 3
lopphind = hind2 *1.4
print(f"Kolme toote hind on {lopphind}")

#pitsa
pitsa = 12.9
pitsa2 = pitsa * 1.1
lopppitsa = pitsa2/3
print(f"Igaüks peab maksma {lopppitsa} pitsa eest")

#rulluisutajad
kiirus = 29.9
kiirus2 = 29.9/60
kaugus = kiirus2 * 24
print(f"Rulluisutaja jõuab {kaugus:1.2f}km kaugusele")

#kolmnurga hüpotenuus
a = 16
b = 9
hupotenuus = a*a + b*b
lopphupotenuus = math.sqrt(hupotenuus)
print(f"Kolmnurga hüpotenuus on {lopphupotenuus:1.2f}")

#ajateisendus
aeg = int(input("Sisestage aeg minutites:  "))
aeg2 = aeg/60
loppaeg = aeg%60

print(f"{aeg2:1.0f}:{loppaeg}")


#kütusekulu
kutus = int(input("Sisestage tagitud kütus liitrites:  "))
km = int(input("Sisestage läbitud kilomeetrid:  "))
loppkutus = kutus/(km/100)

print(f"Kütusekulu on {loppkutus}")



