def sacar(valor):
    numero = int(input("Digite o número da conta: "))
    senha = int(input("Digite a senha: "))

    if numero == 123 and senha == 456:
        saldo = 500

        if saldo >= valor:
            print("valor sacado!")
            print("retire o seu dinheiro na boca do caixa.")
        else:
            print("Saldo insuficiente!")
    else:
        print("Número da conta ou senha incorretos!")
    
def depositar(valor):
    numero = int(input("Digite o número da conta: "))
    senha = int(input("Digite a senha: "))

    if numero == 123 and senha == 456:
        saldo = 500
        saldo += valor
        print(f"Depósito realizado! Novo saldo: {saldo}")
    else:
        print("Número da conta ou senha incorretos!")
sacar(1000)
depositar(200)

