# Leitura das listas de clientes de cada projeto
linha1 = input().strip()
linha2 = input().strip()

# Converta cada linha em um conjunto de nomes
# O split() separa os nomes por espaços; o set() remove duplicatas internas
clientes_projeto1 = set(linha1.split()) if linha1 else set()
clientes_projeto2 = set(linha2.split()) if linha2 else set()

# Identificação dos nomes exclusivos usando a operação de diferença simétrica
# Isso pega o que tem em um, mas não no outro (exclusividade)
exclusivos = clientes_projeto1.symmetric_difference(clientes_projeto2)

# Impressão dos nomes exclusivos em ordem alfabética, ou "Nenhum" se estiver vazio
if exclusivos:
    # sorted() organiza em ordem alfabética e join() junta com espaços
    print(' '.join(sorted(exclusivos)))
else:
    print("Nenhum")
    