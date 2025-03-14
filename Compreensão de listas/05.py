import random

lista = random.sample(range(0,50),10) #usando o metodo random para gerar 10 números de 0 a 50
lista_2 = [i * 2 for i in lista] #usando compreensão de listas para preencher uma lista com os números dobrados

print(f'lista gerada: {lista}') #mostrando a lista gerada aleatoriamente
print(f'Lista com os valores dobrados: {lista_2}') #mostrando os valores dobrados dos números 