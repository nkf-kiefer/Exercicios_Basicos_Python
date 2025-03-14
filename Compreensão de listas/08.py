lista = ["natalia","julia","Gabriel","Teixeira"]#definindo uma lista com algumas palavras

lista_2 = [palavras[::-1] for palavras in lista] #usando ::-1 para inverter os caracteres de cada palavra na lista

print(lista_2) #mostrando o resultado