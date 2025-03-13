lista = [] #declarando uma lista vazia

for i in range(4): #iterando 4 vezes 
    coleta = int(input("Digite um número inteiro qualquer: ")) #coletando os dados
    lista.append(coleta) #armazenando os dados
    
soma_total = sum(lista) #usando a função sum para somar todos os itens da lista

print(f"A soma dessa lista completa é: {soma_total}") #mostrando a soma total