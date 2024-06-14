altura = float(input('Qual a sua altura? Por exemplo, 1.65m ou 2.10m: '))
peso = float(input('Qual o seu peso? Por exemplo, 47.00kg ou 97.50kg: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Você está com peso ideal')
elif imc > 25 and imc <= 30:
    print('Você está com sobrepeso')
elif imc > 30 and imc <= 40:
    print('Você está com obesidade')
else:
    print('Você está com obesidade mórbida')