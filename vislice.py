import bottle
import model

vislice= model.Vislice('stanje.json')

@bottle.get("/") 
def index():
    return bottle.template('index.tpl')

@bottle.post('/igra/')
def nova_igra():
    id= vislice.nova_igra() 
    bottle.redirect('/igra/{}/'.format(id))

@bottle.get('/igra/<id_igre:int>/')
def pokazi_igro(id_igre):
    igra, stanje = vislice.igre[id_igre]
    return bottle.template('igra.tpl',igra=igra, stanje=stanje ,id_igre=id_igre)

@bottle.post('/igra/<id_igre:int>/')
def ugibaj(id_igre):
    crka= bottle.request.forms.getunicode('crka')
    vislice.ugibaj(id_igre, crka)
    bottle.redirect('/igra/{}/'.format(id_igre))    



@bottle.post('/nova_igra/')
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.response.set_cookie('id_igre', str(id_igre), path='/')
    bottle.redirect('/igra/')


@bottle.get('/igra/')
def pokazi_igro():
    id_igre = int(bottle.request.get_cookie('id_igre'))
    igra, stanje = vislice.igre[id_igre]
    return bottle.template('igra.tpl',igra=igra, stanje=stanje ,id_igre=id_igre)


@bottle.post('/igra/')
def ugibaj_2():
    id_igre= int(bottle.request.get_cookie('id_igre'))
    crka= bottle.request.forms.getunicode('crka')
    vislice.ugibaj(id_igre, crka)
    bottle.redirect('/igra/')






@bottle.get('/img/<picture>')
def serve_picture(picture):
    return bottle.static_file(picture, root="img")

bottle.run(debug=True, reloader=True)
