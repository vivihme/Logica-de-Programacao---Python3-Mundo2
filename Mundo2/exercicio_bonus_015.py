s = 0
for c in range (1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s = s + n
print('A soma dos números digitados, e que são par, é {}'.format(s))