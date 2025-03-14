# Criando uma matriz 3x3 com números de 1 a 9
# A matriz será representada por uma lista de listas
# Usamos uma compreensão de listas aninhada para isso

# Parte externa da compreensão de listas: define o início de cada linha
# range(1, 10, 3) cria os valores iniciais 1, 4 e 7, que serão usados para criar cada linha
matriz = [
    # Parte interna da compreensão de listas: cria cada linha com 3 números consecutivos
    [i for i in range(j, j+3)]  # Cria uma lista de números de j até j+2
    for j in range(1, 10, 3)    # Itera pelos valores 1, 4, 7 (início de cada linha)
]

# Exibindo cada linha da matriz no console
for linha in matriz:
    # Imprime cada linha (sublista) individualmente
    print(linha)
