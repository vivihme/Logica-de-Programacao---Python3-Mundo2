numero = int(input('Digite um valor inteiro: '))
opcao = int(input('''Selecione a base numérica para a qual você deseja convertê-lo: 
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL
Sua opção: '''))

if opcao == 1:
    print('O número inteiro {} em binário é igual a {}'.format(numero, bin(numero) [2:]))
elif opcao == 2:
    print('O número inteiro {} em octal é igual a {}'.format(numero, oct(numero) [2:]))
else:
    print('O número inteiro {} em hexidecimal é igual a {}'.format(numero, hex(numero) [2:]))

""" -- COMENTÁRIO: SEM FATIAMENTO
numero = int(input('Digite um valor inteiro: '))
opcao = int(input('''Selecione a base numérica para a qual você deseja convertê-lo: 
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL
Sua opção: '''))

if opcao == 1:
    print('O número inteiro {} em binário é igual a {}'.format(numero, bin(numero)))
elif opcao == 2:
    print('O número inteiro {} em octal é igual a {}'.format(numero, oct(numero)))
else:
    print('O número inteiro {} em hexidecimal é igual a {}'.format(numero, hex(numero)))
"""