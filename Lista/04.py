lista = [] #iniciando uma lista sem nenhum valor

for i in range(3): #fazendo um loop de 3 vezes
    coleta = int(input("Digite um número: ")) #coletando os dados
    lista.append(coleta) #adicionando todos os dados em uma lista

lista.insert(1,50) #usando o metódo insert para adiconar um número em uma posição especifica
print(f"Eita trolei você, agora a sua lista é essa: {lista}") #mostrando a lista