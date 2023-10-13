n = 0
m = 0
for i in range(1, 5):
    notas = float(input(f'Digite sua {i}ª nota: '))
    n += notas
    m = n / 4
print(f'Sua média, é: {m:.1f}')
