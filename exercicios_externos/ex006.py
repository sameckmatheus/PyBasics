import array

vogais = array.array('u', ['a', 'e', 'i', 'o', 'u'])
letra = input('Digite uma letra: ')

letra = letra.lower()

if letra in vogais:
    print(f'A letra {letra} é vogal.')
else:
    print(f'A letra {letra} é consoante.')
