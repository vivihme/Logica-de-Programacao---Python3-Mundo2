cont = 0
N_elementos = int(input('Quantos termos da sequência de Fibonacci você quer exibir? '))
N1 = 0
N2 = 1
print('{} -> {}'.format(N1, N2), end = '')
cont = 3
while cont <= N_elementos:
    N3 = N1 + N2
    print(' -> {}'.format(N3), end = '')
    N1 = N2
    N2 = N3
    cont = cont + 1
print(' -> FIM')