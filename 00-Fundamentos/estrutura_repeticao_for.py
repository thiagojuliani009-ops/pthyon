texto = input("Informe um texto: ")
VOGAIS = "aeiou"

for letra in texto:
    if letra.lower() in VOGAIS:
        print(letra, end="")
else:
    print()

for numero in range(0, 51, 5):
    print(numero, end=" ")