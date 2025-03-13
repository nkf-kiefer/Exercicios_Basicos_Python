lista = [] #criando uma lista vazia

for i in range(7): #iterando 7 vezes
    coleta = int(input("Digite qualquer número inteiro: ")) #coletando os números
    lista.append(coleta) #armazenando os números na lista

lista.sort()#metodo para deixar a lista na ordem crescente

print(f"Sua lista na ordem crescente será de: {lista}") #mostrando a lista em ordem crescente
