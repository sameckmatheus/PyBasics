texto = input("Digite um texto: ")
limite_caracteres = 10

if len(texto) <= limite_caracteres:
    print("Texto dentro do limite de caracteres.")
else:
    print("Texto excede o limite de caracteres.")
