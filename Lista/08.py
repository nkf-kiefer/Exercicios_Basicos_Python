lista = [] #criando uma lista zerada

for i in range(3): #iterando por 3 vezes 
    coletando = int(input("Digite um número qualquer: ")) #coletando os números
    lista.append(coletando)#armazenando na lista os números

lista.reverse() #usando o metódo reverse para alterar a lista
print(f"Eita! Te trolei, a sua lista agora é essa:{lista}") #mostrando a lista atual