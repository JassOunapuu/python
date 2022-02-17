# Jass Õunapuu
#  16.02.2022
#    IT-21

erakonnad = []
kesk = 0
ref = 0
print(f"{'Eesnimi':10} {'Perenimi':10} {'Erakond':10} {'Number':10}  ")

with open('s6pru_l6ustaraamatus.txt', 'r') as minu_fail:
    for rida in minu_fail:
        for i in (rida):
            enimi, pnimi, erakond, number = (rida.split(" "))
        print(f"{enimi:10} {pnimi:10} {erakond:10} {number:10}")
        if erakond == "RE":
            ref += 1
        elif erakond == "KE":
            kesk += 1
        
        if erakond not in erakonnad:
            erakonnad.append(erakond)
        with open('kirjutamine.txt','a') as fail_kirjutamiseks:
            fail_kirjutamiseks.write(str(enimi)+" "+str(pnimi)+'\n')


print( )
print(f"reformikad: {ref}")
print(f"keskmised: {kesk}")
print(f"Erakondi kokku: {len(erakonnad)}")


        




