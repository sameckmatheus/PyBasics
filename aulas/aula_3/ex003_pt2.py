import array

meses = array.array('u', ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
numero = input('Digite um número: ')

if numero in meses:
    print(f' {numero} é vogal.')
else:
    print(f'O número {numero} é inválido.')
