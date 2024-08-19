def contar_palavras(frase):
    palavras = frase.split()
    return len(palavras)

texto = input("Digite uma frase: ")

num_palavras = contar_palavras(texto)
print(f"A frase tem {num_palavras} palavras.")