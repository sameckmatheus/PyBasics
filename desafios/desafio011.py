# Crie um programa que simule o jogo da forca.

name_art = r'''

 #######  #####   ######     ####     ###
  ##   # ### ###   ##  ##   ##  ##   ## ##
  ##     ##   ##   ##  ##  ##       ##   ##
  ####   ##   ##   #####   ##       ##   ##
  ##     ##   ##   ## ##   ##       #######
  ##     ### ###   ## ##    ##  ##  ##   ##
 ####     #####   #### ##    ####   ##   ##

'''

class Forca:
    def __init__(self, palavra, limite):
        self.palavra = palavra
        self.limite = limite

    def palavras(self):
        palavra = input('Você deve escolher uma palavra para que os outrospossam adivinhar.\n'
                        'Digite a palavra que você escolheu: ')
        ...

    def tentativas(self):
        ...


forca = Forca()
print(name_art)