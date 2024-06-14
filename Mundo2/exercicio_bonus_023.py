from random import randint
from time import sleep
computador = randint(0,10)
jogo = 0
tentativas = 0

while jogo != computador:
    print('----- VAMOS JOGAR -----')
    jogo = int(input('Pensei em um número de 0 a 10. Tente adivinhar: '))
    print('PROCESSANDO...')
    sleep(2)
    tentativas = tentativas + 1
    #SE O JOGADOR VENCEU + EXIBIÇÃO DE TENTATIVAS
    if jogo == computador:
        print('Você é fera! Eu pensei no número {}'.format(computador))
        print('Foi necessário você tentar {} vez(es)'.format(tentativas))
    else:
        print('Venci! Eu pensei em outro número, não no {}'.format(jogo))