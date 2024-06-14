from datetime import date
ano_corrente = date.today().year
contS = 0
contN = 0
for n in range (1, 8):
    ano_nascimento = int(input('Em qual ano a {}ª nasceu? '.format(n)))
    idade = ano_corrente - ano_nascimento
    maioridade = 21
    if idade >= maioridade:
        contS = contS + 1
    else:
        contN = contN + 1
print('Ao todo, tivemos {} pessoa(s) que alcançaram a maioridade penal, e {} pessoa(s) que não'.format(contS, contN))