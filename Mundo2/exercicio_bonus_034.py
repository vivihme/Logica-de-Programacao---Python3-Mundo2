maior_idade = menor_idade_feminino = total_masculino = 0
while True:
    print('-=' * 15)
    print('CADASTRE UMA PESSOA')
    idade = int(input('Qual a sua idade? '))
    if idade > 18:
        maior_idade = maior_idade + 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o seu sexo? [M/F]: ')).strip().upper()[0]
        if sexo == 'M':
            total_masculino = total_masculino + 1
        elif sexo == 'F' and idade < 20:
            menor_idade_feminino = menor_idade_feminino + 1
    print('--- CADASTRO FEITO COM SUCESSO ---')
    novo_cadastro = ' '
    while novo_cadastro not in 'SN':
        novo_cadastro = str(input('Você quer fazer um novo cadastro? [S/N]: ')).strip().upper()[0]
    if novo_cadastro == 'N':
        break
print('O número de pessoas com mais de 18 anos é {}'.format(maior_idade))
print('O total de homens cadastrados é {}'.format(total_masculino))
print('O número de mulheres com menos de 20 anos é {}'.format(menor_idade_feminino))