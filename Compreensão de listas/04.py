import random

lista = random.sample(range(0,100),10) #criando uma lista com 10 números de 0 a 100
lista_2 = [i for i in lista if i < 50] #fazendo a compreensão de lista

print(f"Números gerados na lista 1: {lista}") #mostrando o resultado
print(f"Números menores que 50 gerados na lista 1: {lista_2}") #mostrando o resultado