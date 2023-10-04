notas = [''] * 5

for _ in range(5):
    notas[_] = float(input(f'Informe a {_+1}ª nota: '))

soma = 0
for i in range(5):
    soma += notas[i]

media = soma / 5
acima_media = 0
for j in range(5):
    if notas[j] > media:
        acima_media += 1

print(media)
print(soma)
print(acima_media)
