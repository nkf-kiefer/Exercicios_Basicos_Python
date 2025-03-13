lista_1 = [] #iniciando uma lista vazia

for i in range(4): #iterando 4 vezes
    coletando_1 = int(input("Digite um número qualquer: ")) #coletando números
    
    if coletando_1 % 2 == 0: #realizando a verificação se o número possui resto = 0 quando dividido por 2
        lista_1.append(coletando_1) #armazenando na lista apenas os números pares

print(f"A lista que você passou possui esses números pares: {lista_1}")