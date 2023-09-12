# Faça um programa que receba um número e usando laços de repetição calcule e mostre a tabuada desse número.

n = int(input('Digite um número: '))
for a in range(1, 11):
    print(f'{n} x {a} = {n * a}')
