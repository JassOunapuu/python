#  Jass Õunapuu
#   02.03.2022
#     IT21


# 17. email
import re

email = input("Sisestage oma email kujul enimi.pnimi@server.com:  ")

loop=0
while loop == 0:
    if "@" in email:
        enimi,pnimiServer,com = email.split(".")
        pnimi,server = pnimiServer.split("@")
        print(f"Tere {enimi}, sinu email on {server} serveris ja domeeniks on sul {com}")
        loop = 1
    else:
        email = input("Kirjutasite emaili valesti, proovige uuesti (enimi.pnimi@server.com):  ")
        
    


