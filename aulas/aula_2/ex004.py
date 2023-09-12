while True:
    litros = float(input('Informe a quantidade de litros vendidos: '))
    tipo_g = input('Informe o tipo de combustível (G) para gasolina ou (E) para etanol: ')

    # tipo_g = tipo_g.upper() transforma os caracteres minúsculos em maiúsculos
    # tipo_g = tipo_g.lower() transforma os caracteres maiúsculos em minúsculos

    if tipo_g == 'G' or tipo_g == 'g':
        gasolina = 5.80 * litros
        print(f'O valor a ser pago, é: R$ {gasolina:.2f}')

    elif tipo_g == 'E' or tipo_g == 'e':
        etanol = 4.90 * litros
        print(f'O valor a ser pago, é: R$ {etanol:.2f}')

    else:
        print('Entrada inválida!!!')
        print('Insira uma das opções informadas anteriormente...')

    continuar = input('\nSe desejar sair, digite (q). '
                      '\nSe não, pressione (Enter) para novo cálculo: \n')
    if continuar == 'q':
        break
