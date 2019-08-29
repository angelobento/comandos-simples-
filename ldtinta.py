largura=float(input("largura da parede:"))
altura=float(input("altura da parede:"))
area = largura*altura
cores = {'limpo':'\033[m',#comando par cor \0033[m
         'azul':'\033[34m',
         'vermelho':'\033[31m',
         'roxo':'\033[35m',}
tinta = area / 2
print("Sua parede tem uma dimensão de {}{:.2f}{}m X {}{:.2f}{}m, e a sua área é de {}{:.2f}{}m \n para pintar essa parede você ira precisar de {}{}{} litros de tinta".format(cores['azul'], largura, cores['limpo'], cores['vermelho'], altura, cores['limpo'], cores['roxo'], area, cores['limpo'], cores ['roxo'], tinta, cores['limpo']))

#esse comando calcula os litros de tinta necessario para pinar uma parede onde cada litro de tinta cobre 2m de parede.


























