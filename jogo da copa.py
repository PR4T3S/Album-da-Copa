import functions

cash = functions.cash
pack = functions.pack

print(20*'=' + " Bom dia Senhor(a) " + 20*'=')

while True:
    try:
        if colantes == 682:
            print("Parabéns Senhor(a)!!!!!!!!!!\nVocê completou o álbum.!!!!!!!!!")
            print("Até o próximo álbum.")
    except NameError:
        pass
    try:
        option = int(input("""   Você possui: R$%i,00 e %i pacotes
=======================================
    O que deseja fazer: 
       [1] Comprar pacotes.
       [2] Abrir pacotes.
       [3] Detalhes sobre o álbum.
       
       [0] Sair
    
    >>> """%(cash,pack)))
    except ValueError:
        print("Opção inválida!\n")
        continue

    if option < 0 or option > 4:
        print("Opção inválida!\n")

    if option == 1:
        print("\nSe deseja sair digite 0, caso contrário, apenas clique 'enter':")
        while True:
            compra = input("\t>>> ")
            if compra == '0':
                print(39*"=")
                break
            elif compra != '':
                print("\tOpção Inválida.\n\tTente Novamente...\n")
                continue
            else:
                if cash <= 1:
                    print("\tNão é possível comprar mais pacotes.\n\tVocê não possui dinheiro suficiente.\n")
                    print(39*"=")
                    break
                cash -= 2
                functions.register_cash(cash)
                print("\tVocê comprou 1 pacote.\n")
                pack += 1
                functions.register_pack(pack)

    if option == 2:
        print("Apenas clique 'enter' para abrir cada pacote, caso queira sair, digite 0:")
        while True:
            abrir = input("\t>>> ")
            if abrir == '0':
                print(39*"=")
                break
            elif abrir != '':
                print("\tOpção Inválida.\n\tTente novamente...\n")
            else:
                if pack == 0:
                    print("\tVocê não tem pacotes para abrir.\n\tPor favor, compre mais pacotes.\n")
                    print(39*"=")
                    break
                pack -= 1
                functions.register_pack(pack)
                cards = functions.pack_cards()
                print("\tNo pacote veio as seguintes figurinhas:", cards)
                for i in cards:
                    functions.register_cards(i)
                print("\tForam coladas as figurinhas não repetidas.")
                continue

    if option == 3:
        colantes = 0
        locais = [r'cards\cards0.txt',r'cards\cards1.txt',r'cards\cards2.txt',r'cards\cards3.txt',r'cards\cards4.txt',r'cards\cards5.txt',r'cards\cards6.txt']
        for i in locais:
            colantes += functions.pick_colantes(i)
        print("\tVocê possui no seu álbum %i figurinhas coladas.\n\tFaltam %i figurinhas para completar."%(colantes,682-colantes))
        print("\tVocê possui %i de figurinhas repetidas.\n"%(functions.pick_repetidas()))
        print(39 * "=")

    if option == 0:
        print("Até mais Senhor(a)!!")
        break
