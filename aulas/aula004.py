nome = input('Digite seu nome: ')
idd = int(input('Digite sua idade: '))
sal = float(input('Digite seu salário: '))
aumento = sal + (sal/5)

message = (f'O seu nome, é: {nome}.\n'
           f'Sua idade, é: {idd}.\n'
           f'E o seu salário, é: {sal}.\n'
           f'Após o aumento de 20%, seu salário agora é de: ')
print(message)
