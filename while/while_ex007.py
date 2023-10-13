continuar = 'Ss'
while continuar in 'Ss':

    base = float(input('Informe o valor da base: '))
    while base == 0:
        base = float(input(f'\nA medida da base, não pode ser 0. Informe outro valor: '))

    altura = float(input('Informe o valor da altura: '))
    while altura == 0:
        altura = float(input(f'\nA medida da altura, não pode ser 0. Informe outro valor: '))

    area = (base * altura) / 2
    print(f'A área do triângulo, é: {area} cm²\n')

    continuar = input('Deseja realizar um novo cálculo? Digite (s/n): ')
    if continuar in 'Nn':
        print('Obrigado por utilizar meu programa!')
        break
