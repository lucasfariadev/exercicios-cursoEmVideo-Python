num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('__'*30)
print(f'a lista vompleta é: {num}')
print(f'a lista de pares é: {pares}')
print(f'A lista de impares é: {impares}')