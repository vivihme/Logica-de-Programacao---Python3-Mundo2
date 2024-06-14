nome = str(input('Qual o seu nome? '))
if nome == 'Gustavo':
    print('Muito prazer, Gustavo. Seu nome é belíssimo')
elif nome == 'Martha':
    print('Muito prazer, Martha. Gosto muito do seu nome')
else:
    print('Muito prazer, {}'.format(nome))