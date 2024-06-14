'''
c = 1
while c < 10:
    print(c)
    c = c + 1
print('FIM')
'''
'''
n = 1
while n != 0: #FLAG / PONTO DE PARADA
    n = int(input('Digite um valor: '))
print('FIM')
'''
'''
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
print('FIM')
'''
n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else: 
            impar = impar + 1
print('FIM')
print('Você digitou {} número(s) par, e {} número(s) impar'.format(par, impar))