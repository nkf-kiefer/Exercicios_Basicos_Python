lista = [] #iniciando uma lista zerada

for i in range(4): #looping 4 vezes
    coleta = int(input("Digite um número qualquer: ")) #coletando os números
    lista.append(coleta) #armazenando os números em uma lista
    if coleta == 20: #caso algum número digitado seja 20
        lista.remove(20) #exlui o número 20 da lista

print(f"Sua lista é essa: ",*lista) #mostrando a lista