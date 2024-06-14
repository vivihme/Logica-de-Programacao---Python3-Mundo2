from random import randint
from time import sleep
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0,2)

opcao = int(input('''Vamos jogar JOKENPO:
====================== 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual você escolhe? '''))
print('======================')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('O computador escolheu {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[opcao]))

if opcao == 0: #você jogou Pedra
    if opcao == 0 and computador == 2:
        print('Parabéns, você venceu!')
    elif opcao == 0 and computador == 0:
        print('Opa, deu empate!')
    else:
        print('Que pena, você perdeu!')
if opcao == 1: #você jogou Papel
    if opcao == 1 and computador == 0:
        print('Parabéns, você venceu!')
    elif opcao == 1 and computador == 1:
        print('Opa, deu empate!')
    else:
        print('Que pena, você perdeu!')
if opcao == 2: #você jogou Tesoura
    if opcao == 2 and computador == 1:
        print('Parabéns, você venceu!')
    elif opcao == 2 and computador == 2:
        print('Opa, deu empate!')
    else:
        print('Que pena, você perdeu!')