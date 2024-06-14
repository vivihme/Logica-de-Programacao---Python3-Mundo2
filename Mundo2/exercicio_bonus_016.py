#PROGRRESSÃO ARTIMÉTICA QUE MOSTRA OS DEZ PRIMEIROS TERMOS

primeiro_termo = int(input('Digite o termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = primeiro_termo + (11 - 1) * razao
for c in range (primeiro_termo, decimo, razao):
    print(c)
print('FIM')