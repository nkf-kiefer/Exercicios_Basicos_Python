lista = [] #definindo uma lista vazia

for i in range(4): #iterando 3 vezes
    coletando = int(input("Digite números inteiros: ")) #coletando os dados
    lista.append(coletando) #armazenando os dados

lista.insert(4, 99) #inserindo na posiçao 4 o número 99

print(f"Essa lista é: {lista}") #mostrando o resultado