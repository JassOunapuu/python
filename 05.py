# Jass Õunapuu
#  15.02.2022
#    IT-21


# Vanused/Tärnid

vanused = [74,15,24,68,172,56,42,89,57]

for i in range(len(vanused)):
    print("*" * vanused[i])
print()



print(f"kõige vanem: {max(vanused)}")
print(f"kõige noorem: {min(vanused)}")
print(f"kõik vanused kokku: {sum(vanused)}")
print(f"keskmine: {sum(vanused)/len(vanused):10.2f}")

print()






# Duplikaadid

opilased = ['Juhan','Kati','Mario','Mario','Mati','Mati']

p_opilased = []

for i in range(len(opilased)):
    if opilased[i] not in p_opilased:
        p_opilased.append(opilased[i])
for i in range(len(p_opilased)):
    print(p_opilased[i])



# Õpilased

print()

opilased = ['Juhan','Kati','Maarja','Mario','Mati']

for i in range(len(opilased)):
    print(f"{i+1} {opilased[i]}")
valik = int(input("Millist nime tahate muuta? (1/2/3/4/5):   "))
del opilased[valik-1]
nimi = input("Sisestage uus nimi:  ")
opilased.insert(valik-1,nimi)
for j in range(len(opilased)):
    print(opilased[j])


# Nimede lisamine loendisse

nimed = []

for i in range(5):
    nimi = input("Sisesta nimi:  ")
    nimed.append(nimi)
nimed.sort()
for j in range(len(nimed)):
    print(nimed[j])