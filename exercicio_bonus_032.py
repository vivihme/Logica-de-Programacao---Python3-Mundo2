while True:
    num = int(input('Você deseja ver a tabuada de qual número? '))
    if num < 0:
        break
    print('-' * 30)
    for cont in range(1,11):
        print('{} x {} = {}'.format(num, cont, num * cont))
        cont = cont + 1
    print('-' * 30)
print('-' * 30)
print('PROGRAMA ENCERRADO')