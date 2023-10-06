"""
17.As maçãs custam R$ 1,30 cada se forem
compradas menos de uma dúzia, e R$ 1,00
se forem compradas pelo menos 12. Escreva um
programa que leia o número de maçãs
compradas, calcule e escreva o custo total da compra
"""
nMacas = int(input('Informe a quantidade de maçãs que deseja: '))
if nMacas >= 12:
    mensagem = f'Valor total da compra: R$ {nMacas*1:.2f}'
    print(mensagem)
else:
    mensagem = f'Valor total da compra: R$ {nMacas*1.30:.2f}'
    print(mensagem)
