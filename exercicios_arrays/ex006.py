'''Faça um código para ler 5 números e
armazenar em um vetor. Após a leitura
total dos 5 números, o código deve
escrever esses 5 números lidos na ordem
inversa'''

num = [0]*5

for i in range (5):
    n = int(input(f"Digite o {i+1}º número:  "))
    num[i] = n

for j in range (4,-1,-1):
    print(num[j], end = " ")