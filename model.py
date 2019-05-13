import random


STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = "+"
PONOVLJENA_CRKA = "o"
NAPACNA_CRKA = "-"
ZMAGA = "W"
PORAZ = "X"

class Igra:
    def __init__(self,niz,seznam=[]):
        self.geslo = niz
        self.crke = seznam

    def napacne_crke(self):
        seznam_napacnih=[]
        for crka in self.crke:
            if crka not in self.geslo:
                seznam_napacnih.append(crka)
        return seznam_napacnih

    def pravilne_crke(self):
        seznam_pravilnih=[]
        for crka in self.crke:
            if crka in self.geslo:
                seznam_pravilnih.append(crka)
        return seznam_pravilnih

    def stevilo_napak(self):
       return len(self.napacne_crke())

    def zmaga(self):
        for crka in self.geslo:
            if crka not in  self.crke:
                return False
        return True
               

    def poraz(self):
        return self.stevilo_napak() >= STEVILO_DOVOLJENIH_NAPAK
            

    def pravilni_del_gesla(self):
        niz = ""
        for crka in self.geslo:
            if crka in self.crke:
                niz += crka + " "
            else:
                niz += "_ "
        return niz 


    def nepravilni_ugibi(self):
        niz = ""
        for crka in self.crke:
            if crka not in self.geslo:
                niz += crka + " "
        return niz    

    def ugibaj(self,crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crka)
            if crka in self.pravilne_crke():
                if self.zmaga():
                    return ZMAGA
                else:
                    return PRAVILNA_CRKA
            else:
                if self.poraz:
                    return PORAZ
                else:
                    return NAPACNA_CRKA


bazen_besed = []
with open("besede.txt", "r") as nabor_besed:
    for vrstica in nabor_besed:
        bazen_besed.append(vrstica.strip().upper())

def nova_igra():
    return Igra(random.choice(bazen_besed))
