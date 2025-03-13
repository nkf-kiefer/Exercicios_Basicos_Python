lista = [] #criando uma lista vazia

for i in range(3): #realizando a iteração
    coleta = int(input("Digite números inteiros qualquer: ")) #coletando os dados 
    lista.append(coleta) #armazenando os dados na lista

menor = min(lista) #usando a função min para achar o menor número

print(f"O maior número da lista é: {menor}") #mostrando o resultado