# Definir uma palavra secreta aleatória
palavra_secreta = escolher_uma_palavra()

# Inicializar uma lista de letras acertadas com traços
letras_acertadas = ["_" para cada letra em palavra_secreta]

# Inicializar uma lista de letras erradas vazia
letras_erradas = []

# Inicializar uma variável de erros com zero
erros = 0

# Inicializar uma variável de acertos com zero
acertos = 0

# Inicializar uma variável de fim de jogo com falso
fim_de_jogo = falso

# Enquanto o jogo não terminar, repetir os seguintes passos:
enquanto não fim_de_jogo:

  # Mostrar as letras acertadas e as letras erradas na tela
  mostrar(letras_acertadas)
  mostrar(letras_erradas)

  # Pedir ao usuário para digitar uma letra ou a palavra inteira
  chute = ler_entrada()

  # Se o chute for igual à palavra secreta, mostrar uma mensagem de vitória e encerrar o jogo
  se chute == palavra_secreta:
    mostrar("Parabéns, você ganhou!")
    fim_de_jogo = verdadeiro

  # Senão, se o chute for uma letra, verificar se ela está na palavra secreta
  senão se chute é uma letra:

    # Se a letra já foi chutada antes, mostrar uma mensagem de aviso e continuar o jogo
    se chute está em letras_acertadas ou letras_erradas:
      mostrar("Você já tentou essa letra antes!")

    # Senão, se a letra está na palavra secreta, atualizar as letras acertadas e aumentar os acertos
    senão se chute está em palavra_secreta:
      atualizar(letras_acertadas, chute)
      acertos = acertos + 1

      # Se os acertos forem iguais ao tamanho da palavra secreta, mostrar uma mensagem de vitória e encerrar o jogo
      se acertos == tamanho(palavra_secreta):
        mostrar("Parabéns, você ganhou!")
        fim_de_jogo = verdadeiro

    # Senão, se a letra não está na palavra secreta, atualizar as letras erradas e aumentar os erros
    senão:
      atualizar(letras_erradas, chute)
      erros = erros + 1

      # Mostrar o desenho da forca de acordo com os erros
      desenhar_forca(erros)

      # Se os erros forem iguais a sete, mostrar uma mensagem de derrota e encerrar o jogo
      se erros == 7:
        mostrar("Puxa, você foi enforcado!")
        mostrar("A palavra era " + palavra_secreta)
        fim_de_jogo = verdadeiro

  # Senão, se o chute não for uma letra nem a palavra inteira, mostrar uma mensagem de erro e continuar o jogo
  senão:
    mostrar("Entrada inválida!")

# Fim do pseudo código
