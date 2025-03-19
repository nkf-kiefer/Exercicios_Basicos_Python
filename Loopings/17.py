frase = input('Digite uma frase: ')

vogal = 'aeiou'
cont = 0

for letra in frase: #percorrendo toda a string
    if letra in vogal: #filtrando se na string ocorre a aparição de alguma vogal
        cont += 1 #contando quantas vezes apareceu vogais

print(f"Na frase: {frase} foram encontradas {cont} vogais")