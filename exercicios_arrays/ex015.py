"""
15. Escreva um algoritmo para ler dois
valores (considere que não serão lidos
valores iguais) e escrevê-los em ordem
crescente
"""
n1 = int(input(f'Digite o 1º valor: '))
n2 = int(input(f'Digite o 2º valor: '))
if n1 == n2:
    print('valores iguais não são aceitos.')
    quit()
elif n1 > n2:
    print(n2, n1)
else:
    print(n1, n2)
