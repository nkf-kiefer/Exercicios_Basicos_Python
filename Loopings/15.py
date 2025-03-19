numeros = [] #iniciando uma lista vazia

while True:
    numero = int(input("Digite números e caso queira parar digite 0: "))
    #pedindo ao usuário que digite números até que se ele quiser parar basta digitar 0
    if numero == 0: #realizando a condição
        break
    numeros.append(numero) #armazenando os números na lista


print(f'Você digitou os seguintes números: {numeros}')
