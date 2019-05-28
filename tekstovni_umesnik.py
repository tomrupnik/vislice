from model import *

def izpis_igre(igra):
    return ''' Stevilo preostalih poskusov: {}, napacne crke so {}, pravilni del gesla {}
    '''.format(STEVILO_DOVOLJENIH_NAPAK-igra.stevilo_napak(),igra.napacne_crke(),igra.pravilni_del_gesla())


def izpis_zmage(igra):
    return''' Cestitam igra je koncana, beseda je bila {}
    '''.format(igra.geslo)

def izpis_poraza(igra):
    return''' Igra je na zalost koncana, beseda je bila {}
    '''.format(igra.geslo)

def zahtevaj_vnos(igra):
    return input('vnesi crko: ')
def pozeni_vmesnik(igra):
    igra= nova_igra()

