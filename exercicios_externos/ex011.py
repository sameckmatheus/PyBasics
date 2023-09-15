"""
Percorrendo dicionários...

neste exemplo podemos ver disferentes formas de impressão de resultados. Onde, no comando:
    print(tabela_produtos[produto])
Podemos fazer a impressão não apenas do rótulo (ex: "faca") do dicionário, mas, também de seu valor atribuido
(ex:
    "faca": # valor atribuido -> 10
).
O que não acontece no comando:
    print(produto)
Que, embora correto, no informa apenas os rótulos dentro da chave do dicionário (tabela_produtos)
"""

tabela_produtos = {
    "faca": 10,
    "cafeteira": 200,
    "panela": 35,
    "frigideira": 60,
    "garfo": 10,
}

for produto in tabela_produtos:
    print(produto)
    print(tabela_produtos[produto])
