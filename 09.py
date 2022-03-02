# Jass Õunapuu
#  28.02.2022
#    IT-21



#kuupäevad
import datetime
date = datetime.datetime.now()

print(date.strftime("%d. March %Y"))
print()
print(date.strftime("%d. Märts %Y"))
print()

#vanuse leidmine isikukoodi abil
kood ="5020824642"  #pole tegelik isikukood
aasta = int(kood[1]+kood[2])+2000
kuu = int(kood[3]+kood[4])
paev = int(kood[5]+kood[6])

date2 = date.strftime("%Y,%m,%d")
aa,mm,dd = date2.split(",")

from dateutil.relativedelta import relativedelta
start_date = datetime.datetime(aasta,kuu,paev)
end_date = datetime.datetime(int(aa),int(mm),int(dd))
difference_in_years = relativedelta(end_date, start_date).years
print(f"Oled {difference_in_years}. aastane")
