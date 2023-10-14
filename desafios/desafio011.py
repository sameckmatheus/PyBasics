import os

name_art = (r"""
    forca
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
        os.system('clear' if os.name == 'posix' else 'cls')  # Limpa o terminal
        print('Você deve escolher uma palavra para que os outros possam adivinhar.')
        palavra_secreta = input('Digite a palavra que você escolheu: ')
        os.system('clear' if os.name == 'posix' else 'cls')  # Limpa o terminal novamente após a entrada

        self.palavra_secreta = palavra_secreta.lower()
        self.letras_corretas = ["_" for _ in self.palavra_secreta]

    def verificar_chute(self, chutes):
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
        if self.erros == 0:
            return "Nenhum erro ainda."
        elif self.erros == 1:
            return r""" 
                +---+
                |   |
                O   |
                    |
                    |
                    |
                    ========="""
        elif self.erros == 2:
            return r"""
                +---+
                |   |
                O   |
                |   |
                    |
                    |
                    ========="""
        elif self.erros == 3:
            return r"""
                +---+
                |   |
                O   |
               /|   |
                    |
                    |
                    ========="""
        elif self.erros == 4:
            return r"""
                +---+
                |   |
                O   |
               /|\  |
                    |
                    |
                    ========="""
        elif self.erros == 5:
            return r"""
                +---+
                |   |
                O   |
               /|\  |
               /    |
                    |
                    ========="""
        elif self.erros == 6:
            return r"""
                +---+
                |   |
                O   |
               /|\  |
               / \  |
                    |
                    ========="""


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
