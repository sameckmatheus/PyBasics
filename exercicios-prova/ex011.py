"""
11. Faça um algoritmo que leia a idade de
uma pessoa expressa em anos, meses e dias
e escreva a idade dessa pessoa expressa
apenas em dias. Considerar ano com 365
dias e mês com 30 dias.
"""
idade = int(input('Informe sua idade (anos): '))
meses = int(input('Informe sua idade (meses): '))
dias = int(input('Informe sua idade (dias): '))
soma = idade*365+meses*30+dias

print(f'Você viveu {soma} dias.')
