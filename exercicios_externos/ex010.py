"""
calcule o valor referente aos impostos elegidos sobre os produtos a seguir, considerando que o imposto corresponde a
10% do valor total do produto:
- Faca              R$ 10,00;
- Cafeteira         R$ 200,00;
- Panela            R$ 20,00;
- Frigideira        R$ 50,00;
- Garfo             R$ 10,00;
"""

lista_precos = [10, 200, 20, 50, 10]

for preco in lista_precos:
    imposto = preco * 0.1
    print(f'O imposto sobre o produto, é: R$ {imposto:.2f}')
