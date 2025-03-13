lista = [] #iniciando uma lista sem nada

for i in range(2): #looping
    coleta = int(input("Digite 2 números: ")) #coletando 2 números
    lista.append(coleta) #armazenando na lista

lista.pop(1)#cortando o último número digitado

print(f"Eita te trolei de novo, sua lista possui esses números: {lista}")