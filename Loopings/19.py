import random

lista_1 = [random.randint(0,100) for i in range(5)] #randomizando a lista 
lista_2 = [random.randint(0,100) for i in range(5)] #randomizando a lista

for elemento1, elemento2 in zip(lista_1,lista_2): #percorrendo ambos os elementos de ambas as listas
    print(f'Número da lista 1 {lista_1} e número da lista 2 :{lista_2}') #mostrando o resultado
