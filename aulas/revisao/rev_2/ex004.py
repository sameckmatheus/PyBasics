loop = 'S'
while loop == 'S' or loop == 's':
    n = int(input('Digite um número: '))
    opcao = input('Digite: \n'
                  '(1) para o antecessor.\n'
                  '(2) para o sucessor.\n'
                  '(3) para encerrar o programa: ')

    if opcao == '1':
        print('\n=================================================')
        print(f'O número que você foi {n}.\n'
              f'O seu antecessor, é {n-1}.')
        print('=================================================')

    elif opcao == '2':
        print('\n=================================================')
        print(f'O número que você foi {n}.\n'
              f'E o seu sucessor, é {n + 1}.')
        print('=================================================')

    elif opcao == '3':
        print('\n=================================================')
        print('Obrigado por utilizar nosso programa!')
        print('=================================================')
        quit()

    else:
        print('\n===================')
        print('OPÇÃO INVÁLIDA!!!')
        print('===================')

    loop = input('\nDeseja verificar novamente?\n'
                 'Escolha uma das opções (s/n): ')

    if loop == 'N' or loop == 'n':
        print('\n=================================================')
        print('Obrigado por utilizar nosso programa!')
        print('=================================================')
        break

