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
