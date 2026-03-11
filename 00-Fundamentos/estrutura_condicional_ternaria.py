saldo = 2000
saque = 1500

status = "Sucesso!" if saldo >= saque else "Saldo insuficiente!"

print(f"Saque: {status} ao realizar o saque!")
