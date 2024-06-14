frase = str(input('Digite uma frase qualquer: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Não temos um palíndromo')