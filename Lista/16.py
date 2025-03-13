lista = [] #definindo uma lista vazia

for i in range(3): #iterando 3 vezes
    coletando = int(input("Digite números inteiros: ")) #coletando os dados
    lista.append(coletando) #armazenando os dados

tamanho = len(lista) #função len para medir o tamanho da lista

print(f"O tamanho dessa lista é: {tamanho}") #mostrando o resultado