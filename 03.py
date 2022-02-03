# Harjutus 3
# J. Õunapuu
# 03.02.2022



#palindroom


pal = input("Sisesta palindroom:  ")
print(pal == pal[::-1])


#tundide ajad
start = input("Algusaeg:")
lopp = input("Lõpuaeg:")

#tükeldus
hh1,mm1 =start.split(":")
hh2,mm2 =lopp.split(":")

#teisendamine minutiteks
minutid = int(hh1)*60+int(mm1)
minutid2 = int(hh2)*60+int(mm2)

#absoluutväärtus
ajavahe = abs(minutid-minutid2)

#teisendamine hh:mm
hh = ajavahe // 60 #täisarvuline jagamine
mm = ajavahe % 60 #jääk

#lause vormindamine format abil
print(f"Õpilase päeva pikkus on {hh}:{mm}")



#emaili kontroll
#TRUE/FALSE in/not in

email = input("Sisesta email:  ")
print('@' in (email))


#vandumine
vanne = input("Ära kurat ütle:  ")
vanne = vanne.lower().replace("kurat","*****")

print(vanne)


#korralik kasutajanimi
nimi = input("sisesta nimi:  ")
nimi = nimi.strip().capitalize()
print ("Tere "+nimi+"!")