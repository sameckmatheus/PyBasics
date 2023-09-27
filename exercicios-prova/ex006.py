"""
6. Ler um valor e escrever a mensagem É MAIOR
QUE 10! se o valor lido for maior que 10, caso
contrário escrever NÃO É MAIOR QUE 10!
"""
n = int(input('Digite um número: '))
if n > 10:
    mensagem = f'O número {n} é maior que 10.'
    print(mensagem)
else:
    mensagem = f'O número {n} não é maior que 10.'
    print(mensagem)

