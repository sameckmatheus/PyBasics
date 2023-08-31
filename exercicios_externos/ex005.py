n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
calc = input('Selecione a operação: ')

if calc == '+':
    soma = n1 + n2
    res = 'A soma entre {} e {} é igual a {}'.format(n1, n2, soma)
    print(res)

if calc == '-':
    sub = n1 - n2
    res = 'A subtração entre {} e {} é igual a {}'.format(n1, n2, sub)
    print(res)

if calc == '*':
    multi = n1 * n2
    res = 'A multiplicação entre {} e {} é igual a {}'.format(n1, n2, multi)
    print(res)

if calc == '/':
    div = n1 / n2
    res = 'A divisão entre {} e {} é igual a {}'.format(n1, n2, div)
    print(res)
