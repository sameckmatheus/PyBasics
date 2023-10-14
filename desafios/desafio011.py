name_art = (r"" "\n"
            r"" "\n"
            r" #######  #####   ######     ####     ###" "\n"
            r"  ##   # ### ###   ##  ##   ##  ##   ## ##" "\n"
            r"  ##     ##   ##   ##  ##  ##       ##   ##" "\n"
            r"  ####   ##   ##   #####   ##       ##   ##" "\n"
            r"  ##     ##   ##   ## ##   ##       #######" "\n"
            r"  ##     ### ###   ## ##    ##  ##  ##   ##" "\n"
            r" ####     #####   #### ##    ####   ##   ##" "\n"
            r"" "\n")


class Forca:
    def __init__(self, palavra_secreta):
        self.palavra_secreta = palavra_secreta
        self.erros = 0
        self.acertos = 0
        self.fim = False
        self.letras_corretas = ["_"]
        self.letras_erradas = []

    def definir_palavra_secreta(self, palavra_secreta):
        segredo = input('Você deve escolher uma palavra para que os outros possam adivinhar.\n'
                        'Digite a palavra que você escolheu: ')
        palavra_secreta = segredo
        return palavra_secreta

    def verificar_chute(self, palavra_secreta, update):
        chute = input('Digite uma letra: ')
        if chute == palavra_secreta:
            return "Parabéns, você venceu!"
        
        elif chute in self.letras_corretas:
            return "Você já tentou essa letra antes!"
        
        elif chute in palavra_secreta:
            update(self.letras_corretas, chute)
            self.acertos += 1

        else:
            update(self.letras_erradas, chute)
            self.erros += 1

    def draw_art(self):
        if self.erros == 1:
            return r"""+---+
                       |   ||
                       O   ||
                           ||
                           ||
                           ||
                       ========="""
        elif self.erros == 2:
            return r"""+---+
                       |   ||
                       O   ||
                       |   ||
                           ||
                           ||
                       ========="""
        elif self.erros == 3:
            return r"""+---+
                       |   ||
                       O   ||
                      /|   ||
                           ||
                           ||
                       ========="""
        elif self.erros == 4:
            return r"""+---+
                       |   ||
                       O   ||
                      /|\  ||
                           ||
                           ||
                       ========="""
        elif self.erros == 5:
            return r"""+---+
                       |   ||
                       O   ||
                      /|\  ||
                      /    ||
                           ||
                       ========="""
        elif self.erros == 6:
            return r"""+---+
                       |   ||
                       O   ||
                      /|\  ||
                      / \  ||
                           ||
                       ========="""
        elif self.erros > 6:
            return ("Infelizmente, você perdeu..."
                    "a palavra era ", self.palavra_secreta)


forca = Forca(palavra_secreta=1)
print(name_art)
