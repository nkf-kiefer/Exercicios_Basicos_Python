lista = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,-0,1,2,3,4,5,6,7,8,9,10] #definindo uma lista
cont = 0

for i in lista: #percorrendo a lista
    if i < 0: #verificando se é negativo
        cont += 1 #contando quantas vezes um negativo apareceu
print(f"A lista possui {i} números negativos")
