lista = [] #iniciando uma lista zerada

for i in range (5): # realizando um looping 5 vezes
 recebe = float(input("Digite 5 números aleatórios: ")) #coletando os dados
 lista.append(recebe) #adicionando na lista os números digitados usando a função append 
 
print(f"O terceiro elemento da sua lista é: {lista[2]}") #mostrando o 3 elemento da lista