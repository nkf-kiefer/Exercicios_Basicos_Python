import random

# Gerar uma lista com 20 números aleatórios entre 0 e 100
aleatorio = [random.randint(0, 100) for i in range(20)]

# Iterar pelos números e interromper o loop se encontrar um número maior que 50
for numero in aleatorio:
    if numero > 50:
        print(f"Número maior que 50 encontrado: {numero}")
        break
    print(f"Número atual: {numero}")
