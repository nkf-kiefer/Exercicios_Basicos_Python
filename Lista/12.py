lista_1 = [] #criando uma lista vazia
lista_2 = [] #criando uma segunda lista vazia

for i in range(2):
    coletando_1 = int(input("Digite qualquer número inteiro aleatório: ")) #coletando os dados
    lista_1.append(coletando_1) #armazenando os 2 números numa lista

for i in range(3): 
    coletando_2 = int(input("Digite mais números inteiros: "))#coletando os dados
    lista_2.append(coletando_2) #armazenando outros 3 números em uma outra lista 

ajuntando = lista_1 + lista_2 #ajuntando as listas

print(f"As duas listas juntas: {ajuntando}") #mostrando as listas juntas