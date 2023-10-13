# Crie uma lista vazia e adicione 5 elementos a ela.
# Observação:
# Lembrando que, apesar da estrutura estar correta, pelo fato da lista estar vazia se faz necessário o uso do método
# append() para adicionar quaisquer elementos a mesma.

lista_elementos = []

for elemento in range(5):
    add_elemento = int(input('Digite algo: '))
    lista_elementos = lista_elementos.append(add_elemento)
print(lista_elementos)
