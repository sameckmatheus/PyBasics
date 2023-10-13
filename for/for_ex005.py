# Faça um programa que mostre as tabuadas dos números de 1 a 10 usando laços de repetição

for n1 in range(1, 11):
    print(f'Tabuada do: {n1}')
    for n2 in range(1, 11):
        print(f'{n1} x {n2} = {n1 * n2}')
    print()
