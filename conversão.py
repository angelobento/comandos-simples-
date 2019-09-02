num = int(input("digite um número inteiro:"))
print('''Escolha uma das bases:
[ 1 ] converter para Binário
[ 2 ] converter para Octal
[ 3 ] converter para Hexadecimal''')

opçao = int(input("sua opção:"))
if opçao == 1:
    print("{} convertido para binário é igual a {}{}".format(num, "\033[31m", bin(num)[2:]))
elif opçao == 2:
    print("{} convertido para Octal é igual a {}{}".format(num, '\033[31m', oct(num)[2:]))
elif opçao == 3:
    print('{} convertido para Hexadecimal é igual a {}{}'.format(num, '\033[31m', hex(num)[2:]))
else:
    print("Opção invalida, tente novamente mais tarde.")

#esse programa converte numeros inteiros para binário, octal ou hexadecimal

















