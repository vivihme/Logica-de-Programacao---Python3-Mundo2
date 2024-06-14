num = cont = soma = 0
while True:
    num = int(input('Digite um número: '))
    print(num)
    if num == 999:
        break
    soma = soma + num
    cont = cont + 1
print('A soma vale {}'.format(soma))

'''
cont = 1
while True:
    print(cont, '-> ', end= '')
    cont = cont + 1
print('Acabou')
'''