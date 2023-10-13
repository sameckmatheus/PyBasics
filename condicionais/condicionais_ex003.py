time1 = input('Informe o primeiro time: ')
sg_1 = int(input('Informe o saldo de gols deste time na partida: '))
time2 = input('Informe o segundo time: ')
sg_2 = int(input('Informe o saldo de gols deste time na partida: '))

if sg_1 == sg_2:
    print(f'{time1} e {time2} EMPATARAM!')
else:
    if sg_1 > sg_2:
        print(f'{time1} foi o vencedor!')
    else:
        print(f'{time2} foi o vencedor!')
