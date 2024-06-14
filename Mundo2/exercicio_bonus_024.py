print('----- PRIMEIRO VALOR -----')
valor1 = int(input('Digite o primeiro valor: '))
print('----- SEGUNDO VALOR ------')
valor2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    #APRESENTE O MENU
    opcao = int(input('''----- MENU DE OPERAÇÕES -----
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA
    Sua opção: '''))
    #OPERAÇÕES
    if opcao > 0 and opcao <= 5:
        if opcao == 1:
            print('A soma entre os dois valores é {}'.format(valor1 + valor2))
        if opcao == 2:
            print('A multiplicação entre os dois valores é {}'.format(valor1 * valor2))
        if opcao == 3:
            if valor1 > valor2:
                print('O maior valor é {}'.format(valor1))
            elif valor1 < valor2:
                print('O maior valor é {}'.format(valor2))
            else:
                print('Os dois valores são iguais')
        if opcao == 4:
            print('Informe os números novamente: ')
            valor1 = int(input('Primeiro valor: '))
            valor2 = int(input('Segundo valor: '))
    if opcao >= 6:
        print('Opção inválida. Tente novamente!')
print('Fim do programa. Volte sempre!')