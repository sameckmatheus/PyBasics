'''Altere o sistema anterior e faça um sistema
de login, pedindo a senha do usuário e
mostrando seu nome e a mensagem, login
efetuado com sucesso.'''


nome_usuario = [0]
senha_usuario = [0]

for x in range (1):
    nome_usuario[x] = input("Digite seu nome: ")
    senha_usuario[x] = input("Digite sua senha: ")

senha = input("Para efetuar o login, digite sua senha: ")

while senha != senha_usuario[x]:
    senha = input("Senha não identificada, tentar novamente: ")
else :
    print(nome_usuario[x],",login efetuado com sucesso!")