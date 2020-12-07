import random
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
print('''\033[36mSuas opções:\033[m
\033[33m[0] PEDRA
[1] PAPEL
[2] TESOURA\033[m''')
jogador = int(input('\033[1;33mQual é sua jogada?\033[m '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('\033[32m-=\033[m'*10)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('\033[32m-=\033[m'*10)

if computador == 0:
    if jogador == 0:
        print('\033[32mEMPATE\033[m')
    elif jogador == 1:
        print('\033[33mJOGADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[31mCOMPUTADOR VENCE\033[m')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('\033[31mCOMPUTADOR VENCE\033[m')
    elif jogador == 1:
        print('\033[32mEMPATE\033[m')
    elif jogador == 2:
        print('\033[33mJOGADOR VENCE\033[m')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('\033[31mCOMPUTADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[32mEMPATE\033[m')
    else:
        print('\033[7;30;47JOGADA INVÁLIDA!\033[m')
