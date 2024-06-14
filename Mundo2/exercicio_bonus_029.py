num = cont_num = cont_total = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        cont_num = cont_num + 1
        cont_total = cont_total + num
    else:
        cont_num = cont_num + 0
        cont_total = cont_total + 0
print('FIM')
print('Você digitou {} números. A soma entre eles é {}'.format(cont_num, cont_total))