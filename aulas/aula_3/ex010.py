"""
    Faça um programa que leia um valor n, inteiro e positivo, calcule e mostre a seguinte soma:
    S = 1 + 1/1 + 1/2 + 1/3 + 1/4 + … + 1/n.

    O programa também deve verificar se o valor de n é realmente inteiro.

    Também deve ser criado um loop para o pragrama, para que o usuário possa realizar quantos testes quiser sem ter que
    rodar o programa várias vezes.
"""

while True:
    a = int(input('Digite um número interiro e positivo: '))
    s = 0
    if isinstance(a, int) and a > 0:
        for i in range(1, a+1):
            s = a + (1 / i)
            print(f'o resultado é: {s}')
    else:
        print('Entrada inválida!!!')

    continuar = input('\nSe deseja encerrar, digite [q].\n'
                      'Ou, digite [Enter] para novo cálculo.\n')
    if continuar == 'q':
        print('<Obrigado por testar meu código!/>')
        break
