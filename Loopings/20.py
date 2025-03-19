import random #importando a biblioteca de randomizar

for i in range(10): #percorrendo 10 vezes como se fosse o lançamento
    resultado = random.randint(1, 6)  # Gera um número aleatório entre 1 e 6 correspondentes a face do dado
    print(f"Lançamento {i + 1}: {resultado}") #mostrando qual foi o lançamento e a face apresentada
