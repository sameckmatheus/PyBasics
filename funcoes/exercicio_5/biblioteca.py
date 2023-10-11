def calcular_media(n1, n2):
    media = (n1 + n2) / 2
    return media


def imprimir_media(nome, media):
    if media >= 7:
        return "APROVADO", nome
    elif media >= 4:
        return "RECUPERAÇÃO", nome
    else:
        return "REPROVADO", nome
