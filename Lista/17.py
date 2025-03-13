lista = [] #declarando uma lista vazia
lista_duplicada = [] #declarando uma lista vazia

for i in range(2): #iterando 2 vezes
    coletando = int(input("Digite números inteiros: ")) #coletando os dados
    lista.append(coletando) #adicionando os dados na lista
for item in lista: 
    lista_duplicada.append(lista) #duplicando a lista


print(f"Lista duplicada = {lista_duplicada}") #mostrando o resultado