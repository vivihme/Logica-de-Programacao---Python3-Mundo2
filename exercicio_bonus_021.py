soma_idade = 0
media_idade = 0
quant_mulher = 0
maior_idade_homem = 0
nome_homem = 0
for c in range (1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Qual o seu nome? '))
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Qual o sexo? M ou F: ')).strip().upper()
# -- MÉDIA DE IDADE 
    soma_idade = soma_idade + idade
    media_idade = soma_idade / c
# -- MULHERES COM MENOS DE 20 ANOS    
    if (sexo == 'F') and (idade < 20):
        quant_mulher = quant_mulher + 1
# -- HOMEM MAIS VELHO
    if (idade == 1) and (sexo == 'M'):
        maior_idade_homem = idade
        nome_homem = nome
    if  (idade > maior_idade_homem) and (sexo == 'M'):
        maior_idade_homem = idade
        nome_homem = nome
print('A média de idade do grupo é {}'.format(media_idade))
print('A quantidade de mulheres com idade abaixo de 20 anos é {}'.format(quant_mulher))
print('O nome do homem mais velho é {}'.format(nome_homem))