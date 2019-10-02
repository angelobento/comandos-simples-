maior = 0
menor = 0
for k in range(1, 6):
    pseo = float(input("peso da {}ª pessoa:".format(k)))
    if pseo == 1:
        maior =pseo
        menor = pseo
    else:
        if pseo > maior:
            maior = pseo
        if pseo < menor:
            menor =pseo
print("o maior peso é {}".format(maior))
print("o menor peso é {}".format(menor))














