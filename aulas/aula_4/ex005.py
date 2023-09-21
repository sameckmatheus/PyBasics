"""
    Refaça o exercicio anterior, agora
    implementando a pergunta:
    “Deseja realizar novo cálculo?”
"""

while True:

    n1 = float(input('Informe a primeira nota: '))
    while 0 > n1 > 10:
        n1 = float(input('Informe a primeira nota, com valores válidos entre 0 e 10: '))
    n2 = float(input('Informe a segunda nota: '))
    while 0 > n2 > 10:
        n2 = float(input('Informe a segunda nota, com valores válidos entre 0 e 10: '))
    media = (n1 + n2) / 2
    print(f'A sua média foi calculada.\n'
          f'Resultado: {media}')

    continuar = input('\nDeseja sair, digite [q]?\n '
                      'Ou, digite [Enter] para novo cálculo: ')
    if continuar == 'q':
        break
