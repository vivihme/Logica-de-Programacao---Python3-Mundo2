#PROGRRESSÃO ARTIMÉTICA QUE MOSTRA OS DEZ PRIMEIROS TERMOS
print('GERADOR DE PA')
print('-=' * 10)
primeiro_termo = int(input('Digite o termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro_termo
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end = '')
    termo = termo + razao
    cont = cont + 1
print('FIM')