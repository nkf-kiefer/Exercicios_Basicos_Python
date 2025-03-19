import random

lista = [random.randint(0, 100) for i in range(10)]  # Gerando uma lista com 10 números de 0 a 100
print(f'A lista possui esses números: {lista}')

# Filtrar os números maiores ou iguais a 10 usando compreensão de listas
lista = [i for i in lista if i >= 10]

print(f'A lista atualizada (sem números menores que 10) possui esses números: {lista}')
