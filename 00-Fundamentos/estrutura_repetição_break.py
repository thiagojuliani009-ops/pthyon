while True:
    numero = int(input("imforme um número: "))
    if numero == 10:
        break
    if numero % 2 == 0:
        continue
    print(numero)
    