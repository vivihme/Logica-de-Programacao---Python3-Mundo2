cont = 0
valor_sacado = int(input('Qual valor a ser sacado? R$ '))
total = valor_sacado
ced = 50
total_ced = 0
while True:
    if total >= ced:
        total = total - ced
        total_ced = total_ced + 1
    else:
        if total_ced > 0:
            print('Total de {} cédulas de R$ {}'.format(total_ced, ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if total == 0:
            break
print('FIM')
print('Volte sempre ao Banco Curso em Vídeo (BCE)')