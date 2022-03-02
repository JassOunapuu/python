#  Jass Õunapuu
#   02.03.2022
#     IT21

import re




#Leian IP'd

ip=" "

with open('nonsense.txt', 'r') as fail:
    for line in fail:
        if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",line):
            print(line,end="")

#Leian paroolid

with open('nonsense.txt', 'r') as fail:
    for line in fail:
        if re.match("^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$",line):
            print(line,end="")

