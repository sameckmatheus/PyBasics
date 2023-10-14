# Corrigir a formatação da arte do nome
name_art = (r"" "\n"
            r" #######  #####   ######     ####     ###" "\n"
            r"  ##   # ### ###   ##  ##   ##  ##   ## ##" "\n"
            r"  ##     ##   ##   ##  ##  ##       ##   ##" "\n"
            r"  ####   ##   ##   #####   ##       ##   ##" "\n"
            r"  ##     ##   ##   ## ##   ##       #######" "\n"
            r"  ##     ### ###   ##  ##    ##  ##  ##   ##" "\n"  # Corrigir o espaçamento entre as letras
            r" ####     #####   ######      ####   ##   ##" "\n"  # Corrigir os símbolos das letras
            r"" "\n")


class Forca:
    def __init__(self, palavra_secreta):
        self.palavra_secreta = palavra_secreta
        self.erros = 0
        self.acertos = 0
        self.fim = False
        self.letras_corretas = ["_" for _ in palavra_secreta]
        # Inicializar a lista com o mesmo tamanho da palavra secreta
        self.letras_erradas = []

    def definir_palavra_secreta(self):  # Remover o parâmetro palavra_secreta, pois ele não é usado
        segredo = input('Você deve escolher uma palavra para que os outros possam adivinhar.\n'
                        'Digite a palavra que você escolheu: ')
        self.palavra_secreta = segredo  # Atribuir o valor do segredo ao atributo da classe
        return self.palavra_secreta  # Retornar o atributo da classe

    def verificar_chute(self, update):
        # Remover o parâmetro palavra_secreta, pois ele pode ser acessado pelo atributo da classe
        chute = input('Digite uma letra: ')
        if chute == self.palavra_secreta:  # Comparar o chute com o atributo da classe
            return "Parabéns, você venceu!"

        elif chute in self.letras_corretas or chute in self.letras_erradas:
            # Verificar se o chute já foi feito antes em qualquer uma das listas
            return "Você já tentou essa letra antes!"

        elif chute in self.palavra_secreta:  # Comparar o chute com o atributo da classe
            update(self.letras_corretas, chute)  # Atualizar a lista de letras corretas com o chute
            self.acertos += len([letra for letra in self.palavra_secreta if
                                 letra == chute])
            # Aumentar os acertos de acordo com o número de vezes que a letra aparece na palavra secreta

        else:
            update(self.letras_erradas, chute)  # Atualizar a lista de letras erradas com o chute
            self.erros += 1

    def draw_art(self):
        if self.erros == 1:
            return r"""+---+
                        |   |
                        O   |
                            |
                            |
                            |
                        ========="""
        elif self.erros == 2:
            return r"""+---+
                        |   |
                        O   |
                        |   |
                            |
                            |
                        ========="""
        elif self.erros == 3:
            return r"""+---+
                        |   |
                        O   |
                        /|  |
                            |
                            |
                        ========="""
        elif self.erros == 4:
            return r"""+---+
                        |   |
                        O   |
                        /|\ |
                            |
                            |
                        ========="""
        elif self.erros == 5:
            return r"""+---+
                        |   |
                        O   |
                        /|\ |
                        /   |
                            |
                        ========="""
        elif self.erros == 6:
            return r"""+---+
                        |   |
                        O   |
                        /|\ |
                        / \ |
                            |
                        ========="""
        elif self.erros > 6:
            return ("Infelizmente, você perdeu..."
                    "a palavra era " + self.palavra_secreta)  # Concatenar a string com o atributo da classe


forca = Forca(palavra_secreta="")  # Inicializar a palavra secreta com uma string vazia
forca.definir_palavra_secreta()  # Chamar o método para definir a palavra secreta
print(name_art)
