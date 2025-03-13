lista = [] #criando uma lista vazia

for i in range(4): #iterando 2 vezes
    coletando = int(input("Digite números inteiros: ")) #coletando os dados
    lista.append(coletando) #adicionando os dados na lista

    if coletando == 10: #fazendo a condição da ocorrência do 10 na lista
        achar = lista.index(coletando) #usando a função index para coletar o índice

print(f"O primeiro número 10 ocorreu na: {achar} posição") #mostrando o índice