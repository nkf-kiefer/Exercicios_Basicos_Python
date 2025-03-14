# Lista de palavras
palavras = ["Ana", "Eduardo", "Luiza", "Isabela", "Otávio", "Marcelo", "Ursula"]

# Filtrando apenas as palavras que começam com uma vogal
palavras_comecam_com_vogal = [palavra for palavra in palavras if palavra[0].lower() in "aeiou"]

print(palavras_comecam_com_vogal)
