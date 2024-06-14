''''
inicio = int(input('Digite o número de início: '))
fim = int(input('Digite o número de fim: '))
passo = int(input('Digite o número de passo: '))

for c in range (inicio, fim + 1, passo):
    print(c)
print('FIM')
'''
s = 0
for c in range (0, 4):
    n = int(input('Digite um número: '))
    s += n
print('FIM')
print('O somatório de todos os números foi {}'.format(s))