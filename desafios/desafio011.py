import string

name_art = (r"""
 ######   #####   ######     ####     ###
 ##      ##   ##  ###  ##   ##  ##   ## ##
 ##      ##   ##  ##   ##  ##       ##   ##
 #####   ##   ##  ##  ##   ##       ##   ##
 ##      ##   ##  #####    ##       #######
 ##      ##   ##  ## ###    ##  ##  ##   ##
 ##       #####   ##  ###    ####   ##   ##
""")
print(name_art)


class Forca:
    def __init__(self):
        self.palavra_secreta = ""
        self.erros = 0
        self.acertos = 0
        self.fim = False
        self.letras_corretas = []
        self.letras_erradas = []

    def definir_palavra_secreta(self):
        print('Bem-vindo ao Jogo da Forca!')
        palavra_secreta = 'python'
        self.palavra_secreta = palavra_secreta.lower()
        self.letras_corretas = ["_" for _ in self.palavra_secreta]

    def verificar_chute(self, chutes):
        if chutes not in string.ascii_lowercase or len(chutes) != 1:
            return "Por favor, digite apenas uma letra válida."

        if chutes in self.letras_corretas or chutes in self.letras_erradas:
            return "Você já tentou essa letra antes!"

        elif chutes in self.palavra_secreta:
            for i, letra in enumerate(self.palavra_secreta):
                if letra == chutes:
                    self.letras_corretas[i] = chutes
                    self.acertos += 1
            if self.acertos == len(self.palavra_secreta):
                self.fim = True
                return "Parabéns, você venceu!"

        else:
            self.letras_erradas.append(chutes)
            self.erros += 1
            if self.erros >= 6:
                self.fim = True
                return "Infelizmente, você perdeu... a palavra era " + self.palavra_secreta

        return None

    def desenhar_forca(self):
        pass


forca = Forca()
forca.definir_palavra_secreta()

while not forca.fim:
    print("Palavra: " + " ".join(forca.letras_corretas))
    print("Letras erradas: " + ", ".join(forca.letras_erradas))
    print(forca.desenhar_forca())
    chute = input('Digite uma letra: ').lower()
    resultado = forca.verificar_chute(chute)
    if resultado:
        print(resultado)
        break

