from random import randint
computador = randint(0,10)
cont = 0
print('-=-'*13)
print('Vamos jogar PAR ou ÍMPAR')
print(('-=-'*13))
while True:
    jogador = int(input('Digite um número: '))
    op = str(input('Par ou Ímpar?[P/I]')).strip().upper()[0]
    resp = (computador + jogador)
    print('-=-'*20)
    if op == 'P':
        if resp % 2 == 0:
            cont += 1
            print(f'Parabéns! O computador jogou {computador} e você jogou {jogador}. {computador + jogador} é PAR')
            print('-=-'*20)
        elif resp % 2 != 0:
            print('GAME OVER')
            print(f'Que pena! O computador jogou {computador} e você jogou {jogador}. {computador+jogador} é ÍMPAR!')
            print(f'Você venceu {cont} rodadas')
            break
    if op == 'I':
        if resp % 2 !=0:
            cont +=1
            print(f'Parabéns! O computador escolheu {computador} e você jogou {jogador}. {computador+jogador} é ÍMPAR!')
            print('-=-'*20)
        elif resp % 2 == 0:
            print('GAME OVER')
            print(f'Que pena! O computador jogou {computador} e você jogou {jogador}. {computador+jogador} é PAR!')
            print(f'Você venceu {cont} rodadas')
            break
print('~'*20)
print('obrigado por jogar')