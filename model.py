import random
import json

STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = "+"
PONOVLJENA_CRKA = "o"
NAPACNA_CRKA = "-"
ZMAGA = "W"
PORAZ = "X"
ZACETEK = "Z"

class Igra:
    def __init__(self,niz,seznam=None):
        self.geslo = niz
        if seznam is None:
            self.crke = []
        else:
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
                if self.poraz():
                    return PORAZ
                else:
                    return NAPACNA_CRKA


bazen_besed = []
with open("besede.txt", "r") as nabor_besed:
    for vrstica in nabor_besed:
        bazen_besed.append(vrstica.strip().upper())

def nova_igra():
    return Igra(random.choice(bazen_besed))


class Vislice:
    def __init__(self,datoteka_s_stanjem):
        self.igre={}
        self.datoteke_s_stanjem = datoteka_s_stanjem


    def prost_id_igre(self):
        if self.igre == {}:
            return 1
        else:
            return max(self.igre.keys()) + 1

    def nova_igra(self):
        id = self.prost_id_igre()
        igra = nova_igra()
        self.igre[id]= (igra, ZACETEK)
        self.zapisi_igre_v_datoteko()
        return id

    def ugibaj(self,id,crka):
        igra, _ = self.igre[id]
        stanje= igra.ugibaj(crka)
        self.igre[id]= (igra, stanje)



    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem) as f:
            igre = json.load(f)
            self.igre ={}
            for id_igre, vrednosti in igre.items():
                self.igre[int(id_igre)] = (igra(vrednosti['geslo'], crke=vrednosti['crke']), vrednosti['poskus'])

    def zapisi_igre_v_datoteko(self):
        with open(self.datoteke_s_stanjem, 'w') as f:
            igre = {}
            for id_igre, (igra,stanje) in self.igra.items():
                igre[id_igre]= {'geslo': igra.geslo, 'crke' : igra.crke, 'poskus': stanje}
                json.dump(igre,f)
