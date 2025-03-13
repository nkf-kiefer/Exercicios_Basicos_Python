import random #importando a biblioteca random afim de gerar números aleatorios

lista = [random.randint(1, 100) for i in range(10)] 
#da biblioteca random usamos a função .randit para gerar números aleatorios dentro do espaço de 1 a 100
# Percorremos com um looping o total de 10 vezes para gerar os 10 números aleatorios
                                                    
print(lista) #mostramos os 10 números 