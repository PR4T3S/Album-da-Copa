from random import randint

def pick_cash():
    arq_cash = open(r"cash.txt")
    cash = int(arq_cash.readline())  # pegando o dinheiro do arquivo
    arq_cash.close()
    return cash

def pick_pack():
    arq_pack = open(r"pacotes.txt")
    pack = int(arq_pack.readline())  # pegando a quantidade de pacotes
    arq_pack.close()
    return pack

cash = pick_cash()
pack = pick_pack()

def register_cash(x):
    arq_cash_r = open(r"cash.txt")
    arq_cash_w = open(r"cash.txt", "w")
    arq_cash_w.write(str(x))          # registrando o dinheiro
    arq_cash_w.close()
    arq_cash_r.close()

def register_pack(x):
    arq_pack_r = open(r"pacotes.txt")
    arq_pack_w = open(r"pacotes.txt", "w")
    arq_pack_w.write(str(x))          # registrando os pacotes
    arq_pack_r.close()
    arq_pack_w.close()

def pack_cards():  # gerando pacotes aleatórios
    cards = [randint(0,681),randint(0,681),randint(0,681),randint(0,681),randint(0,681)]
    while True:
        p = 0
        for i in cards:
            if cards.count(i) != 1:
                cards.remove(i)
                cards.append(randint(0,681))
                break
            else:
                p += 1
        if p == 5:
            break
    return cards

def page_cards(local,y):
    r = open(local,"r")
    nums = r.readline().split(";")
    nums.remove('')
    if nums.count(str(y)) == 0:
        nums.append(y)
        texto = ""
        for i in nums:
            texto += str(i) + ";"
        w = open(local,"w")
        w.write(texto)
        r.close()
        w.close()
    else:
        print("\tA figurinha %i é repetida."%(y))
        print("\tEla foi colocada no pacote de repetidas.")
        r_repet = open(r"cards\repetidas.txt","r")
        texto = r_repet.readline() + str(y) + ";"
        w_repet = open(r"cards\repetidas.txt","w")
        w_repet.write(texto)
        w_repet.close()
        r_repet.close()

def register_cards(x):
    if x <= 100:
        page_cards(r"cards\cards0.txt",x)
    if x > 100 and x <= 200:
        page_cards(r"cards\cards1.txt", x)
    if x > 200 and x <= 300:
        page_cards(r"cards\cards2.txt", x)
    if x > 300 and x <= 400:
        page_cards(r"cards\cards3.txt", x)
    if x > 400 and x <= 500:
        page_cards(r"cards\cards4.txt", x)
    if x > 500 and x <= 600:
        page_cards(r"cards\cards5.txt", x)
    if x > 600 and x <= 681:
        page_cards(r"cards\cards6.txt", x)

def pick_colantes(local): # pegar número de fig coladas no album
    pre_colantes = []
    arq_colantes = open(local)
    colantes_0 = arq_colantes.readline().split(";")
    arq_colantes.close()
    try:
        colantes_0.remove('')
    except ValueError:
        pass
    colantes_0 = [int(i) for i in colantes_0]
    for i in colantes_0:
        pre_colantes.append(i)
    return len(pre_colantes)

def pick_repetidas(): # pegar num de fig repetidas
    repetidas = []
    arq_repetidas = open(r"cards\repetidas.txt")
    repetidas_0 = arq_repetidas.readline().split(";")
    arq_repetidas.close()
    try:
        repetidas_0.remove('')
    except ValueError:
        pass
    repetidas_0 = [int(i) for i in repetidas_0]
    for i in repetidas_0:
        repetidas.append(i)
    return len(repetidas)