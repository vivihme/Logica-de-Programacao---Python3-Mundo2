num = int(input('Digite um número: '))
tot = 0
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot = tot + 1
    else:
        print('\33[31m', end='' )
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divísivel {} vez(es)'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele NÃO é PRIMO')