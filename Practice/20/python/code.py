class napitok:
    def __init__(self):
        self.name = ''
        self.price = 0.0
        self.voluem = 0.0
deneg = int(input())
kovlo_napitkov = int(input())
chto_poidet_na_buhich = napitok()
vvod_nap = napitok()
k = 0
for i in range (kovlo_napitkov):
    a, b, c = map(str, input().split(' '))
    b = int(b)
    c = int(c)
    a1,b1,c1 = a,b,c
    vvod_nap.name, vvod_nap.price, vvod_nap.voluem = a, b, c
    litrov = (deneg // vvod_nap.price) * vvod_nap.voluem
    if litrov == 0:
        continue
    if k == 0:
        chto_poidet_na_buhich.name, chto_poidet_na_buhich.price, chto_poidet_na_buhich.voluem = a1,b1,c1
        k += 1
    skolko_litrov_luchshe = (deneg // chto_poidet_na_buhich.price) * chto_poidet_na_buhich.voluem
    if litrov > skolko_litrov_luchshe:
        chto_poidet_na_buhich = vvod_nap
if chto_poidet_na_buhich.price == 0:
    print('-1')
else:
    print(chto_poidet_na_buhich.name, deneg // chto_poidet_na_buhich.price)
    print(deneg // chto_poidet_na_buhich.price * chto_poidet_na_buhich.voluem)
    print(deneg - chto_poidet_na_buhich.price * (deneg // chto_poidet_na_buhich.price))