num = int(input("digite um numero: "))
for k in range (1, num + 1):
    if num % k == 0:
        print("\033[33m", end='')
    else:
        print("\033[34m", end='')
    print("{}".format, end=' ' )



































