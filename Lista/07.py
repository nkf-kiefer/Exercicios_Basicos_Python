lista = [] #iniciando uma lista zerada

for i in range(5): #realizando a iteração 5 vezes
    coleta = int(input("Digite um número aleatorio: ")) #coletando os números
    lista.append(coleta) #armazenando os números
    if coleta == 15: #se caso apareça o número 15 ele mostra a mensagem abaixo
        print("Eita nessa lista existe o número 15 !!")

print(f"Sua lista possui esses números: {lista}") #mostrando a lista digitada
