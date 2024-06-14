cont_num = soma_num = media_num = maior_num = menor_num = 0
resposta = 'S'
while resposta == 'S':
    num = int(input('Digite um número: '))
    cont_num = cont_num + 1
    soma_num = soma_num + num
    media_num = soma_num / cont_num
    resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if cont_num == 1:
        maior_num = menor_num = num
    else:
        if num > maior_num:
            maior_num = num
        if num < menor_num:
            menor_num = num
print('FIM')
print('O total de números digitados foi {}. A média entre eles {}'.format(cont_num, media_num))
print('O maior número digitado foi {}, enquanto o menor, {}'.format(maior_num, menor_num))