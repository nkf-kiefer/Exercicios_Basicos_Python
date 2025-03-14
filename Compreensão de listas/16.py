# Lista de temperaturas em Celsius
celsius = [26.5, 37.8, 98.1, 56.7]

# Convertendo para Fahrenheit usando compreensão de listas
conversor = [(i * 9/5) + 32 for i in celsius]

# Exibindo os resultados
print(conversor)
