# comprar passagem de onbius
#cidade origem
#cidade destino
#data saida
#data volta

class Passagem:
    def __init__(self, origem, destino, data_saida, data_volta):
        self.origem = origem
        self.destino = destino
        self.data_saida = data_saida
        self.data_volta = data_volta

def comprar_passagem():
    origem = input("Digite a cidade de origem: ")
    destino = input("Digite a cidade de destino: ")
    data_saida = input("Digite a data de saída (DD/MM/AAAA): ")
    data_volta = input("Digite a data de volta (DD/MM/AAAA): ")

    passagem = Passagem(origem, destino, data_saida, data_volta)
    return passagem
def exibir_passagem(passagem):
    print("\nDetalhes da Passagem:")
    print(f"Origem: {passagem.origem}")
    print(f"Destino: {passagem.destino}")
    print(f"Data de Saída: {passagem.data_saida}")
    print(f"Data de Volta: {passagem.data_volta}")

# Programa principal
if __name__ == "__main__":
    passagem_comprada = comprar_passagem()
    exibir_passagem(passagem_comprada)


  