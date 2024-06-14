reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os segmentos acima podem formar um triângulo')
    if (reta1 != reta2 and reta1 == reta3) or (reta2 != reta1 and reta2 == reta3):
        print('O triângulo é do tipo isósceles')
    elif (reta1 != reta2 and reta1 != reta3) and (reta2 != reta1 and reta2 != reta3):
        print('O triângulo é do tipo escaleno')
    elif reta1 == reta2 and reta1 == reta3:
        print('O triângulo é do tipo equilátero')
else:
    print('Os segmentos acima não podem formar um triângulo')