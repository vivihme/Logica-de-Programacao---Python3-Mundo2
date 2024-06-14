valor_produto = float(input('Qual o valor do produto? R$ '))
forma_pagamento = int(input('''Qual a forma de pagamento? 
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão de crédito/débito
[ 3 ] Em até 2x no cartão de crédito/débito
[ 4 ] Em 3x ou mais no cartão de crédito/débito
SUA OPÇÃO:                            
'''))

if forma_pagamento == 1:
    valor_compra = valor_produto - (valor_produto * 0.1)
    print('Você tem direito a 10% de desconto, logo o valor da sua compra será de R$ {:.2f}'.format(valor_compra))
elif forma_pagamento == 2:
    valor_compra = valor_produto - (valor_produto * 0.05)
    print('Você tem direito a 5% de desconto, logo o valor da compra será de R$ {:.2f}'.format(valor_compra))
elif forma_pagamento == 3:
    valor_compra = valor_produto
    print('O valor da compra será de R$ {:.2f}'.format(valor_compra))
else:
    numero_parcela = int(input('Em quantas vezes deseja parcelar? '))
    valor_compra = valor_produto + (valor_produto * 0.2)
    print('O valor da sua compra terá um acréscimo de 20%, logo o valor da compra será de R$ {:.2f}'.format(valor_compra))