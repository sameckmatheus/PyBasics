""" Ler 10 valores, calcular e escrever a média aritmética desses valores lidos. (usando While) """
soma = 0
contador = 0

while contador < 11:
    valor = float(input('Digite um valor: '))
    soma = soma + valor
    contador = contador + 1

media = soma / contador
print(f'A média aritmética dos valores iseridos, é: {media:.1f}')
