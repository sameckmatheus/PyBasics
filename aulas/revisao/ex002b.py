loop = 'S'

while loop == 'S' or loop == 's':
    n = float(input('Digite um número: '))

    while n == 0:
        n = float(input('Valor inválido, digite outro valor: '))

    else:
        if n > 0:
            print(f"O número {n}, é positivo.")
        else:
            print(f'O número {n}, é negativo.')

    loop = input(
        "\nPressione S para realizar uma nova verificação...\n"
        "Ou, N para encerrar: "
    )
    print()
    if loop == 'N' or loop == 'n':
        break
