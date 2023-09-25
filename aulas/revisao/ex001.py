loop = 'S'

while loop == 'S':
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    media = (n1 + n2) / 2

    if media < 7:
        if media > 4:
            print(f'Sua média foi ({media}).')
            print('Você ficou de RECUPERAÇÃO...')
        else:
            print(f'Sua média foi ({media}).')
            print('Você foi REPROVADO...')
    else:
        print(f'Sua média foi ({media}).')
        print('Você foi APROVADO!!!')

    loop = input(
        "\nPressione S para realizar um novo cálculo...\n"
        "Ou, N para encerrar: "
    )

    if loop == 'N':
        break
