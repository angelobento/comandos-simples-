n = input("digite seu nome:")
corese = {'limpo':'\033[m',
          'azul':'\033[34m',
          'l,bran,f,amare':'\033[7;33m',
          'vermelho':'\033[31m'}
print("ola {}{}{}, prazer!!!".format(corese['l,bran,f,amare'], n, corese['limpo']))




















