from datetime import date
ano_corrente = date.today().year

ano_nascimento = int(input('Qual seu ano de nascimento? '))
idade = ano_corrente - ano_nascimento

if idade <= 9:
    print('Você é um nadador MIRIM')
elif idade >= 10 and idade <= 14:
    print('Você é um nadador INFANTIL')
elif idade >= 15 and idade <= 19:
    print('Você é um nadador JÚNIOR')
elif idade == 20:
    print('Você é um nadador SÊNIOR')
else:
    print('Você é um nadador MASTER')