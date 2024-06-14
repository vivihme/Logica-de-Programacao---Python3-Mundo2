casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário líquido mensal? R$ '))
tempo = int(input('Em quantos meses pretende quitar o empréstimo? '))

prestacao = casa/tempo

if prestacao > salario * 0.3:
    print('Infelizmente, não podemos conceder o empréstimo, pois o valor da prestação ultrapassa 30% do seu salário líquido mensal')
else:
    print('Parabéns! Seu empréstimo foi aprovado')