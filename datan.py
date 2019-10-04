datan= "18/09/2000"
datah= "18/08/2022" # data de hoje

anon=int (datan[6:] )
anoh=int (datah[6:] )
mesn=int (datan[3:5] )
mesh=int (datah[3:5] )
dian=int (datan[0:2] )
diah=int (datah[0:2] )

anos=anoh-anon
if mesn<mesh:
    anos=anos
if mesn>mesh:
    anos = anos -1
else:
    if mesn == mesh and dian > diah:
        anos = anos -1
    if mesn == mesh and dian < diah:
        anos = anos
print ("Você tem {} anos".format(anos))

#esse comaando mostra a sua idade

























