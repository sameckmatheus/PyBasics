loop = 'S'

while loop == 'S':
    n = float(input(
        'Digite um número: '
    ))

    if n > 0:
        print(f"O número {n}, é positivo.")
    elif n < 0:
        print(f'O número {n}, é negativo.')
    elif n == 0:
        print('Valor inválido para a questão...')
        print('Você deve informar um valor diferente de 0')

    loop = input(
        "\nPressione S para realizar uma nova verificação...\n"
        "Ou, N para encerrar: "
    )
    print()
    if loop == 'N':
        break
