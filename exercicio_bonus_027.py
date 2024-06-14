#PROGRRESSÃO ARTIMÉTICA QUE MOSTRA OS DEZ PRIMEIROS TERMOS
print('GERADOR DE PA')
print('-=' * 10)
primeiro_termo = int(input('Digite o termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro_termo
cont = 1
total = 0
mostra_a_mais = 10
while mostra_a_mais != 0:
    total = total + mostra_a_mais
    while cont <= total:
        print('{} -> '.format(termo), end = '')
        termo = termo + razao
        cont = cont + 1
    print('PAUSA')
    mostra_a_mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
print('Progressão finalizada com {} termos mostrados'.format(total))