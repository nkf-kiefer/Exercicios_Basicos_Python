lista = [] #iniciando uma lista zerada

for i in range(5): #loop de 5 números
    numeros = int(input("Digite 5 números:")) #coletando os dados
    lista.append(numeros) #adicionando na lista os números coletados

adiciona = int(input("Digite um último número para colocar na lista: ")) #pedindo um ultimo número
lista.append(adiciona) #adicionando esse último número na lista

print(f"Os números da sua lista são {lista}") #mostrando a lista completa