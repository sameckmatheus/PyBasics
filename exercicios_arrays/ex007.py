'''Faça um código para ler 5 nomes de
usuários e suas respectivas senhas, e
armazenar cada lista em um array
diferente, após completar a digitação,
imprimir , nome, senha e posição dos
dados no array'''

nome_usuario = [0]*5
senha_usuario = [0]*5

for i in range (5):
    nome_usuario[i] = input("Digite seu nome: ")
    senha_usuario[i] = input("Digite sua senha: ")

print(f"\nOS dados das contas seguem: \n")
for j in range (5):
    print(f"O usuario da {j}º posição é {nome_usuario[j]}, e tem a senha: {senha_usuario[j]}")