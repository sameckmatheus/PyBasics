"""12- Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do salário
bruto, mas não é descontado (é a empresa que deposita.)

O salário líquido corresponde ao salário bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

a. Desconto do IR;
b. Salário Bruto ate R$900,00 (inclusive) – Isento;
c. Salário Bruto de R$ 1500, 00 (inclusive) – desconto de 5%;
d. Salario bruto até R$ 2500,00 (Inclusive) – desconto de 10%;
e. Salário bruto acima de 2500 – Desconto de 20%. Imprima na tela as informações, dispostas conforme o exemplo
abaixo, no exemplo valor da hora é 5 e a quantidade de horas é 220.

Salário bruto (5 * 220)           : R$   1100,00
( – ) IR (5%)                     : R$     55,00
( – ) INSS ( 10% )                : R$     110,00
FGTS ( 11%)                       : R$     121,00
Total de descontos                : R$     165,00
Salário Líquido                   : R$     935,00 """

val_hora = float(input('Informe o valor pago por hora trabalhada: '))
horas_mes = float(input('Informe a quantidade de horas trabalhadas no mês: '))
sal_bruto = val_hora * horas_mes
fgts = sal_bruto * 0.11
inss = sal_bruto * 0.10

salb_message = f'O valor do seu salário bruto, é: R$ {sal_bruto:.2f}'
print(salb_message)

if sal_bruto >= 900:
    if sal_bruto <= 1500:
        ir = sal_bruto * 0.05
        total_descontos = ir + inss
        sal_liq = sal_bruto - ir - inss

        message = (f'IR (5%): R$ {ir:.2f}\n'
                   f'INSS (10%): R$ {inss:.2f}\n'
                   f'FGTS (11%): R$ {fgts:.2f}\n'
                   f'Total de descontos: R$ {total_descontos:.2f}\n'
                   f'Salário Líquido: R$ {sal_liq:.2f}')
        print(message)
    elif sal_bruto <= 2500:
        ir = sal_bruto * 0.10
        total_descontos = ir + inss
        sal_liq = sal_bruto - ir - inss

        message = (f'IR (-10%): R$ {ir:.2f}\n'
                   f'INSS (-10%): R$ {inss:.2f}\n'
                   f'FGTS (11%): R$ {fgts:.2f}\n'
                   f'Total de descontos: R$ {total_descontos:.2f}\n'
                   f'Salário Líquido: R$ {sal_liq:.2f}')
        print(message)
    elif sal_bruto > 2500:
        ir = sal_bruto * 0.20
        total_descontos = ir + inss
        sal_liq = sal_bruto - ir - inss

        message = (f'IR (-20%): R$ {ir:.2f}\n'
                   f'INSS (-10%): R$ {inss:.2f}\n'
                   f'FGTS (11%): R$ {fgts:.2f}\n'
                   f'Total de descontos: R$ {total_descontos:.2f}\n'
                   f'Salário Líquido: R$ {sal_liq:.2f}')
        print(message)
else:
    ir = 0
    total_descontos = ir + inss
    sal_liq = sal_bruto - inss
    message = (f'Isento de desconto referente ao IR\n'
               f'INSS (-10%): R$ {inss:.2f}\n'
               f'FGTS (11%): R$ {fgts:.2f}\n'
               f'Total de descontos: R$ {total_descontos:.2f}\n'
               f'Salário Líquido: R$ {sal_liq:.2f}')
    print(message)
