n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
n3 = float(input('Informe a terceira nota: '))

media = (n1 + n2 + n3) / 3

if media < 7:
    if media < 4:
        print(f'Sua média {media:.1f}, foi inferior a 7. Vamos te dar mais uma chance, você está em RECUPERAÇÃO...')
    else:
        print(f'Sua média {media:.1f}, foi inferior a 4. Sinto muito, você foi REPROVADO(A)')
else:
    print(f'Sua média {media:.1f}, foi superior a 7. Parabéns, você foi APROVADO(A)')
