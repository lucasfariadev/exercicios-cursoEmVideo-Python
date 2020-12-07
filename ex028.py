from random import randint
from time import sleep
num = randint(0,5) #faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!... ')
print('-=-' * 20)
usuario = int(input('Que número eu pensei? ')) #jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if usuario == num:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(num, usuario))
