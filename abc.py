#qual maior valor da lista
a = [2,4,5,8,9,7]
nome=["ana,", "beto","cris", "roberto", "maria", "joao"]
n=(len(a))
maior=0
idmaior=0
for k in range (n):
    if a[k]>maior:
        maior=a[k]
        idmaior = k

    print("o maior valor agora é ", maior)
print(" o maior valor é", maior)
print("do(a)", nome[maior])























