soma = 0
acum = 0
for c in range (1, 501):
    if c % 2 == 1 and c % 3 == 0:
        acum = acum + 1
        soma = soma + c
print('FIM')
print('Entre o intervalo de 1 a 500, a quantidade de valores ímpares e divisíveis por 3 é {}, enquanto a soma entre eles é {}'.format(acum, soma))