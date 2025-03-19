def inverter_string(palavra): #usando uma função com variável global 
 return palavra[::-1] #retornando ela ao contrario

palavra = input('Digite uma palavra: ') #coletando uma palavra do usuário
print(f"O inverso dessa palavra é: {inverter_string(palavra)}") #mostrando ao usuário a palavra ao contrário