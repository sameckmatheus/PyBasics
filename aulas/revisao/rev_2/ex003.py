n = []
m = 0
for i in range(1, 5):
    notas = float(input(f'Digite sua {i}ª nota: '))
    n.append(notas)
    m = sum(n) / 4
print(f'Sua média, é: {m:.1f}')
