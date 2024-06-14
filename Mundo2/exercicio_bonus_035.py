cont = total = menor_valor = mais_1000_valor = 0
barato = ' '
while True:
    print('-=' * 15)
    print('INICIE A COMPRA: ')
    nome_produto = str(input('Qual o produto? ')).strip().upper()
    valor_produto = int(input('Qual o valor? '))
    cont = cont + 1
    total = total + valor_produto
    if valor_produto > 1000:
        mais_1000_valor = mais_1000_valor + 1
    #CHECAGEM DO NOME PRODUTO MAIS BARATO
    if cont == 1 or valor_produto < menor_valor:
        menor_valor = valor_produto
        barato = nome_produto
    nova_compra = ' '
    while nova_compra not in 'SN':
        nova_compra = str(input('Deseja fazer mais uma compra? [S/N]: ')).strip().upper()[0]
    if nova_compra == 'N':
        break
print('ENCERRANDO COMPRAS')
print('O total gasto na compra foi R$ {:.2f}'.format(total))
print('O total de produtos que custaram mais de R$ 1 mil é {}'.format(mais_1000_valor))
print('O nome do produto mais barato é {}'.format(nome_produto))