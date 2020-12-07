peso = float(input('Qual é seu peso?(Kg) '))
altura = float(input('Qual é sua altura?(m) '))
imc = peso /(altura) ** 2
print('O IMC dessa pessoa é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso.Cuidado!')
elif imc < 25:
    print('Tudo certo, está no peso ideal!')
elif imc < 30:
    print('Cuidado, sobrepeso')
elif imc < 40:
    print('Cuidado! Obesidade')
else:
    print('Cuidado! Obesidade Mórbida')