import string

# Solicitar nome do ficheiro
nome_ficheiro = input("Introduce o nome do ficheiro .txt: ")

frecuencias = {}

try:
    with open(nome_ficheiro, "r", encoding="utf-8") as f:
        texto = f.read().lower()
        # Eliminar signos de puntuación
        for p in string.punctuation:
            texto = texto.replace(p, "")

        palabras = texto.split()

        # Contar palabras
        for palabra in palabras:
            if palabra in frecuencias:
                frecuencias[palabra] += 1
            else:
                frecuencias[palabra] = 1

    # Mostrar resultados
    print("\nFrecuencia de palabras:")
    for palabra, conta in frecuencias.items():
        print(palabra, ":", conta)

    # Gardar resumo nun ficheiro
    with open("resumo_palabras.txt", "w", encoding="utf-8") as resumo:
        for palabra, conta in frecuencias.items():
            resumo.write(f"{palabra}: {conta}\n")

    print("\nResumo gardado en 'resumo_palabras.txt'.")

except FileNotFoundError:
    print("O ficheiro non existe.")