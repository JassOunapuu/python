# Jass Õunapuu
#  28.02.2022
#    IT-21


class auto:
    #atribuudid
    mark = "teadmata"
    aasta = 0
    hind = 0
    varv = " "
    kiirus = 0
    #meetodid
    def __init__(self,x,y):
        self.mark = x
        self.aasta = y
    
    def kuva(self):
        print("Mark: {} \nAasta: {}".format(self.mark, self.aasta))
        
    def lisaHind(self,x):
        self.hind = x
    
    def kuvaHind(self):
        print("Hind: {}".format(self.hind))
        
    def lisaVarv(self,x):
        self.varv = x
    
    def kuvaVarv(self):
        print("Värv: {}".format(self.varv))
        
    def lisaKiirus(self,x):
        self.kiirus = x
    def kuvaKiirus(self):
        print("Kiirus: {}".format(self.kiirus))


uusObjekt = auto("Tojoota",1969)
uusObjekt.lisaHind("19 999")
uusObjekt.lisaVarv("Kollane")
uusObjekt.lisaKiirus(99)
uusObjekt.kuva()
uusObjekt.kuvaHind()
uusObjekt.kuvaVarv()
uusObjekt.kuvaKiirus()