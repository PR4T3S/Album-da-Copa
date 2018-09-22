from random import randint
import functions
from decimal import Decimal, getcontext

print(53*'=')
print("""Jogue o jogo para ganhar dinheiro e comprar pacotes.
Se acerta: ganha R$1,00
Se perder: perde R$1,00

Boa sorte!!""")
print(53*'=')

cash = functions.cash

while True:
    lim = input("\nSe desejar sair digite 0, caso contrário, clique 'enter':\n>>> ")
    if lim == '0':
        break
    elif lim != '':
        print("\tOpção Inválida.\n\tTente Novamente...\n")
        continue
    else:
        sinais = ["+","-","*","**2","/"]
        sinal = sinais[randint(0,4)]

        if sinal == "+":
            a = randint(0,1000)
            b = randint(0,1000)
            c = randint(0,1000)
            d = randint(0,1000)
            operation = a + b + c + d
            print("Resolva: %i + %i + %i + %i"%(a,b,c,d))
            result = int(input("  > "))
            if result == operation:
                print("Você ganhou R$1,00")
                cash += 1
            else:
                print("Você perdeu R$1,00")
                cash -= 1

        elif sinal == "-":
            a = randint(0,1000)
            b = randint(0,1000)
            c = randint(0,1000)
            d = randint(0,1000)
            operation = a - b - c - d
            print("Resolva: %i - %i - %i - %i"%(a,b,c,d))
            result = int(input("  > "))
            if result == operation:
                print("Você ganhou R$1,00")
                cash += 1
            else:
                print("Você perdeu R$1,00")
                cash -= 1

        elif sinal == "*":
            a = randint(0,1000)
            b = randint(0,1000)
            operation = a*b
            print("Resolva: %i x %i"%(a,b))
            result = int(input("  > "))
            if result == operation:
                print("Você ganhou R$1,00")
                cash += 1
            else:
                print("Você perdeu R$1,00")
                cash -= 1

        elif sinal == "**2":
            a = randint(1,1000)
            operation = a**2
            print("Resolva: %i^2"%(a))
            result = int(input("  > "))
            if result == operation:
                print("Você ganhou R$1,00")
                cash += 1
            else:
                print("Você perdeu R$1,00")
                cash -= 1

        elif sinal == "//":
            a = randint(1,1000)
            b = randint(1,1000)
            operation = a // b
            print("Resolva: %i // %i (Obs: Apenas a parte inteira)"%(a,b))
            result = input("  > ")
            if result == operation:
                print("Você ganhou R$1,00")
                cash += 1
            else:
                print("Você perdeu R$1,00")
                cash -= 1

functions.register_cash(cash)
print("Agora você possui R$%i,00"%(cash))