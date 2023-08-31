n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

soma = n1 + n2
sub = n1 - n2
multi = n1 * n2
div = n1 / n2

calc_message = (f'Os números que você digitou, são: {n1:.0f} e {n2:.0f}\n'
                f'A soma (+) entre {n1:.0f} e {n2:.0f}, é: {soma:.0f}\n'
                f'A subtração (-) entre {n1:.0f} e {n2:.0f}, é: {sub:.0f}\n'
                f'A multiplicação (*) entre {n1:.0f} e {n2:.0f}, é: {multi:.0f}\n'
                f'A divisão (/) entre {n1:.0f} e {n2:.0f}, é: {div:.0f}')
print(calc_message)
