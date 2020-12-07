from time import sleep
num = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        sleep(0.2)
        print('Valor adicionad com sucesso...')
    else:
        print('Valor duplicado: não vou adicionar')
    r = str(input('Quer continuar?[S/N]'))
    if r in 'nN':
        break
print('-=-'*15)
num.sort()
print(f'Você digitou os valores {num}')