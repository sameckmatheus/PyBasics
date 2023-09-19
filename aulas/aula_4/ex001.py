""" Ler 10 valores, calcular e escrever a média aritmética desses valores lidos. (usando While) """
soma = 0
reps = 0

while reps < 11:
    valor = float(input('Diite um valor: '))
    soma = soma + valor
    reps = reps + 1

media = soma / reps
print(f'A média aritmética dos valores iseridos, é: {media:.1f}')
