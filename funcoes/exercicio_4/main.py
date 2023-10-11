def estoque(produto, quantidade, valor_unitario):
    valor_total_estoque = valor_unitario * quantidade
    print(f'O valor total do estoque é de: R$ {valor_total_estoque:.2f}')
    return valor_total_estoque


estoque('feijão', 2, 10)
