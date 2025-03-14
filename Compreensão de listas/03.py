lista = ['natalia','gabriel','tete','juju']
lista_2 = [palavra for palavra in lista if len(palavra) >= 5 ] 
#definindo a primeira aparição de palavra basicamente para ela receber o valor depois da condição for e if
#a segunda aparição palavra serve para percorrer a lista criada anteriormente 
#len(palavra) >= 5 servindo para filtrar somente as palavras com 5 ou mais letras
print(lista_2)