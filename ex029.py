v = float(input('A que velocidade atual do carro: '))
if v > 80.00:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    print('O valor da multa foi de: R${}'.format((v-80.00)*7.00))

print('Tenha um bom dia! Dirija com segurança')