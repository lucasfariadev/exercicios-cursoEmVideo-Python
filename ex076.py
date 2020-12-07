listagem = ('Lapis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 2.5,
            'Transferidor', 4.2,
            'Compasso', 9.99,
            'Mochila', 100.00,
            'Canetas', 22.30,
            'Livro', 34.90)
print('_'*40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print('_'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-=-'*13)
