import random

lista_num_aleatorios = [random.randint(0,100) for i in range(10)]
#gerando uma lista de 10 números aleatórios de 0 a 100

numero_maior = max(lista_num_aleatorios)
#coletando o maior número da lista usando a função max

print(f"O maior número da lista {lista_num_aleatorios} é: {numero_maior}")