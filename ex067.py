while True:
    n = int(input('Quer ver a tabuadade qual valor? '))
    if n < 0:
        break
    print('-' * 30)
    print(f'a tabuada de {n} é:')
    for c in range(1,11):
        print(f'{n} X {c} = {n*c}')
    print('-' * 30)
print('-=-'*20)
print('Programa de tabuada encerrada, volte sempre')