viagem = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(viagem))
#if viagem <= 200:
#    print('E o preço da sua passagem será: R${:.2f}'.format(viagem * 0.50))
#else:
#    print('E o preço da sua passagem será: R${:.2f}'.format(viagem * 0.45))
preço = viagem * 0.50 if viagem <= 200 else viagem * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
