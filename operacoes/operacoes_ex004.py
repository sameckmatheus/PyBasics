nome = input('Digite seu nome: ')
idd = int(input('Digite sua idade: '))
sal = float(input('Digite seu salário: '))
percentual = float(input('Digite qual foi seu percentual de aumento: '))
aumento = sal + ((sal/100)*percentual)

message = (f'O seu nome, é: {nome}.\n'
           f'Sua idade, é: {idd}.\n'
           f'E o seu salário, é: {sal}.\n'
           f'Seu percentual de aumento, é: {percentual:.0f}%.\n'
           f'Após o aumento de 20%, seu salário agora é de: {aumento}')
print(message)
