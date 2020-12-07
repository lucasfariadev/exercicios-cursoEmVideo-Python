num = (int(input('Digite um número: ')),int(input('Digite um número: ')), int(input('Digite um número: ')),  int(input('Digite um número: ')))
print(f'Você digitou os valores {num}')
print(f'o valor 8 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
