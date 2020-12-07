n1 = str(input('Digite seu nome completo: '))
mai = n1.upper()
min = n1.lower()
total = len(n1)
espaços = n1.count(' ')
quan = total - espaços
letras = len(n1.split()[0])
print('Seu nome com todas as letras maíusculas é: {}'.format(mai))
print('Seu nome com todas as letras minúsculas é: {}'.format(min))
print('Seu nome ao todo tem {} letras sem espaço'.format(quan))
print('Seu primeiro nome tem: {} letras'.format(letras))



