import random

lista_alaetoria = [random.randint(0,100)for i in range(10)]
#fazendo uma lista aleatoria de 10 números entre 0 a 100

media = sum(lista_alaetoria) / len(lista_alaetoria)
#calculando a media desses números usando a função sun para fazer a soma dos números e a função len para somar a quantidade de números que apareceram

print(f'A média dos números: {lista_alaetoria} é : {media}')
#mostrando o resultado
