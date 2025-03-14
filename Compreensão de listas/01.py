lista_1 = [i for i in range(0,21)] #utilizando a forma da compreensão de listas [nova_variável for elemento in coleção if condição]
lista_2 = [pares for pares in lista_1 if pares % 2 == 0] 

print(f"A lista 1 contém os números: {lista_1}") #mostrando o resultado
print(f"A lista 2 contém os números pares da lista 1: {lista_2}") #mostrando o resultado

