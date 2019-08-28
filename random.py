from random import randint
computador = randint(0, 5)#faz o computador escolher um numero de tanto a tanto
print("-=-" * 20)
print("tente adivinhar um numero de 0 a 5")
print("-=-" * 20)
jogador = int(input("em que numero eu pensei?"))# jogador adivinha
if jogador == computador:
    print("parabens voce conseguiu!")
else:
    print("ganhei! eu pensei no numero do {} e nao no {}".format(computador, jogador))







