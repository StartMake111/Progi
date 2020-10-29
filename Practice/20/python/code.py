def napitok:
    self.price = 0.0
    self.name = ''
    self.voluem = 0.0

deneg = int(input())
kovlo_napitkov = int(input())

chto_poidet_na_buhich = napitok()

for i in range (kovlo_napitkov):
    napitok.name = input()
    napitok.price= int(input())
    napitok.voluem = int(input())

    litrov  = (deneg // napitok.price) * napitok.voluem

    if litrov == 0:
        continue

    if chto_poidet_na_buhich.price == 0 :
        chto_poidet_na_buhich = napitok
        continue
    skolko_litrov_luchshe = (deneg // chto_poidet_na_buhich.price) * chto_poidet_na_buhich.voluem
    if litrov > skolko_litrov_luchshe:
        chto_poidet_na_buhich = napitok

if chto_poidet_na_buhich.price == 0:
    print('-1')
else:
    print(chto_poidet_na_buhich.name, deneg // chto_poidet_na_buhich.price)
    print(deneg // chto_poidet_na_buhich.price * chto_poidet_na_buhich.voluem)
    print(deneg - chto_poidet_na_buhich.price * (deneg // chto_poidet_na_buhich.price))