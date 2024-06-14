from datetime import date
ano_corrente = date.today().year

nome = str(input('Qual o seu nome completo? '))
sexo = int(input('''Qual o seu sexo? 
[ 1 ] MASCULINO (M)
[ 2 ] FEMININO (F)
Sua escolha: '''))

if sexo == 1:
    ano_nascimento = int(input('Qual seu ano de nascimento? '))
    alistamento = ano_corrente - ano_nascimento

    if alistamento < 18:
        print('Ainda não é tempo hábil de você se alistar nas Forças Armadas brasileiras. Falta {} ano(s)'.format(18 - alistamento))
    elif alistamento == 18:
        print('Você completa 18 anos agora. Está em tempo hábil para se alistar nas Forças Armadas brasileiras')
    else:
        print('O tempo hábil para você se alistar nas Forças Armadas brasileiras passou há {} ano(s)'.format(alistamento - 18))
else:
    print('Você está dispensada! O alistamento militar não é obrigatório para pessoas do sexo feminino')