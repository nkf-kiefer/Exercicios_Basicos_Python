lista = [] #criando uma lista vazia

for i in range(3): #realizando a iteração
    coleta = int(input("Digite números inteiros qualquer: ")) #coletando os dados 
    lista.append(coleta) #armazenando os dados na lista

maior = max(lista) #usando a função max para achar o maior número

print(f"O maior número da lista é: {maior}") #mostrando o resultado