from random import randint
vitoria = 0
print('-=' * 10)
print('VAMOS JOGAR ÍMPAR OU PAR')
print('-=' * 10)
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()
    print(f'Você jogou {jogador} e o computador jogou {computador}. O total é {total}. ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            vitoria = vitoria + 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            vitoria = vitoria + 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print('Você venceu {} vez(es)'.format(vitoria))