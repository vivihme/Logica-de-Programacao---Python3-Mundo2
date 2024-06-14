max = 0
min = 0
for c in range (1, 6):
    peso = float(input('Qual o peso da {}ª pessoa? '.format(c)))
    if c == 1:
        max = peso
        min = peso
    else:
        if peso > max:
            max = peso
        if peso < min:
            min = peso
print('O maior peso foi de {}, enquanto menor foi {}'.format(max, min))
