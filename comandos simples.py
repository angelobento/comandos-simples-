
print("digite a seguir o que quer saber, as opções são: vogal separada, somente vogal e vogal e consoantes.  ATENÇÃO: digite como está escrito nesse recado")
oq=input("o que quer saber?")
frase = (input("digite uma frase:"))#conta quantas vogal e consoantes tem na string
v=frase.count("a")
o=frase.count("e")
g=frase.count("i")
a=frase.count("o")
l=frase.count("u")
vogal = v+o+g+a+l
b=frase.count("b")
c=frase.count("c")
d=frase.count("d")
f=frase.count("f")
G=frase.count("g")
h=frase.count("h")
j=frase.count("j")
k=frase.count("k")
L=frase.count("l")
m=frase.count("m")
n=frase.count("n")
p=frase.count("p")
q=frase.count("q")
r=frase.count("r")
s=frase.count("s")
t=frase.count("t")
V=frase.count("v")
w=frase.count("w")
x=frase.count("x")
y=frase.count("y")
z=frase.count("z")
consoantes= b+c+d+f+G+h+j+k+l+m+n+p+q+r+s+t+V+w+x+y+z
vs= str("vogal separada")
sv= str("somente vogal")
vc =str("vogal e consoantes")
if oq == vs:
    print("sua frase tem {} letras A, {} letras E, {} letras I, {} letras o e {} letras U".format(v,o,g,a,l))
if oq == sv:
    print ("sua frase tem {} vogal".format(vogal))
if oq == vc:
    print("sua frase tem {} vogal e {} consoantes".format(vogal, consoantes))






















