lista = [] #iniciando uma lista vazia

for i in range(3): #iterando 3 vezes
    coletando = int(input("Digite um número inteiro qualquer: ")) #coletando os dados 
    lista.append(coletando) #armazenando na lista

lista.sort(reverse=True) #passando o parâmetro de reverter no metódo sort
print(f"Sua lista em ordem decrescente é: {lista}") #mostrando a lista em forma decrescente