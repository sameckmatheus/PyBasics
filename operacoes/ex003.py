n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
soma = n1 + n2
media = soma/2

message = (f'Os números que vc digitou, são: {n1} e {n2}.\n'
           f'E a soma entre eles é: {soma}.\n'
           f'E a média entre os mesmos é: {media:.0f}.')
print(message)
