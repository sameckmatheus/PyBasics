"""As organizações CSM resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram
para desenvolver o programa que calculará os reajustes.

a. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual;
b. Salários até R$ 280,00 (incluindo): aumento de 20%;
c. Salários entre R$ 280,00 e R$700,00: aumento de 15%;
d. Salários entre R$ 700,00 e R$ 1500,00: aumento de 10%;
e. Salários de R$ 1500,00 em diante: aumento de 5%

- Após o aumento ser realizado;
- informe na tela;

a. O salário antes do reajuste;
b. O percentual de aumento aplicado;
c. O valor do aumento;
d. O novo salário, após o aumento."""

sal_colaborador = float(input('Informe seu salário atual: '))

if sal_colaborador > 0:
    if sal_colaborador <= 280:
        percentual = 20
        val_aumento = sal_colaborador - percentual
        sal_liq = sal_colaborador + percentual

        print(f'Seu salário antes do reajuste, era: {sal_colaborador:.2f}\n'
              f'Seu percentual de aumento aplicado é de {percentual:.1f}%.\n'
              f'O valor do aumento, foi, de: {val_aumento:.2f}\n'
              f'Seu novo salário após o reajuste, é: {sal_liq:.2f}.')

    else:
        pass
else:
    ...
