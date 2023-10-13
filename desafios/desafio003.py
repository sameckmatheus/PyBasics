n = int(input('Digite um número: '))
contador = 0

while contador < n:
    contador += 1
    calc = contador * str(contador)
    print(calc, end='')
    print()
