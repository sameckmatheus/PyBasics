h1 = int(input('h 1: '))
m1 = int(input('m 1: '))
h2 = int(input('h 2: '))
m2 = int(input('m 2: '))

if h1 > 12:
    SomaHora = (h1 + h2) - 12
    SomaMinutos = m1 + m2

    if SomaMinutos > 60:
        SomaHora += 1
        SomaMinutos = SomaMinutos - 60
        print(f'Saída: {SomaHora} : 0{SomaMinutos}')

elif h2 > 12:
    SomaHora = (h1 + h2) - 12
    SomaMinutos = m1 + m2

    if SomaMinutos > 60:
        SomaHora += 1
        SomaMinutos = SomaMinutos - 60
        print(f'Saída: {SomaHora} : 0{SomaMinutos}')

"""
    h1 = 3
    min1 = 45
    h2 = 14
    min2 = 20

    conversao = h2 - 12
    hformat12 = conversao + h1
    mins = min1 + min2

    if mins > 60:
        hformat12 += 1
        gmin = mins - 60

    print(f'Saída: {hformat12}:0{gmin}')
"""
