#mpa()
numero = [1,2,3,4,5]
resultado = list(map(lambda x: x *3, numero))
print (resultado)

numero = [1,2,3,4,5]
resultado = list(map(lambda x: x *5, numero))
print (resultado)

#filter
nota = [6.5, 7.5, 5.9, 10]
resultado = list(filter(lambda nota: nota > 6.0, nota))
print(resultado)

numero = [1,2,3,4,5]
pares = list(filter(lambda x: x % 2 == 0, numero))
print(pares)

#sorted
produtos = [
    {"nome": "notebook", "preco": 3000},
    {"nome": "mouse", "preco": 85},
     {"nome": "tecldo", "preco": 100},

]
ordendo = sorted(produtos, key=lambda p: p["preco"])
print(ordendo)


