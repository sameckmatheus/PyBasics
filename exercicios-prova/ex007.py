"""
7. Faça um código que receba o valor da
base e da altura de um triângulo e
calcule sua área. usando a fórmula A =
(base x Altura ) /2
"""
base = int(input('Informe o valor da base: '))
altura = int(input('Informe o valor da altura: '))
area = (base*altura) / 2

mensagem = f'A área do triângulo, é igual a: {area} cm²'
print(mensagem)
