import random

# Gerar uma lista com 20 números aleatórios
numeros_aleatorios = [random.randint(0, 100) for i in range(20)]
print(f"Lista gerada aleatoriamente: {numeros_aleatorios}")

pares = [num for num in numeros_aleatorios if num % 2 == 0]
print(f"Números pares dessa lista: {pares}")