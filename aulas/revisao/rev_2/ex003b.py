n = 0
m = 0
vezes = int(input('Informe quantos vazes você deseja rodar o programa: '))
for i in range(vezes):
    if vezes >= 1000:
        break  # quit() também pode ser utilizado
    notas = float(input(f'Digite sua {i + 1}ª nota: '))
    while notas > 10 or notas < 10:
        print('As notas precisam ser menores ou iguais a 10.0, e, maiores que 0.')
        notas = float(input(f'Digite sua {i + 1}ª nota: '))
    n += notas
    m = n / vezes
print(f'Sua média, é: {m:.1f}')
