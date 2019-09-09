frase = str(input("digite uma frase:")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for k in range(len(junto)-1, -1, -1):
    inverso += junto[k]
if inverso == junto:
    print("temos um palíndromo!")
else:
    print("a frase nao é um palindromo!")














































