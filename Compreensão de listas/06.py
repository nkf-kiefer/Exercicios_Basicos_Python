lista = "Natália é inteligente e esforçada" #declarando uma frase 

lista_2 = [palavra[0] for palavra in lista.split()]  #definindo palavra[0] para que quando o metódo split for realizado não conte outras letras a não ser a primeira. 
#split é um metódo para partir a string em palavras

print(f"A frase é: {lista}") #mostrando a lista já predefinida
print(f"As letras iniciais de cada palavra são: {lista_2}") #mostrando o resultado