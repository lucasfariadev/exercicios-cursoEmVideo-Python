print('Brasileirão 2018')
times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro',
      'Flamengo', 'Vasco', 'Chapecoense', 'Atlético-PR', 'Bahia',
      'São Paulos', 'Fluminense', 'Sport Recife', 'EC Vitória',
      'Coritiba,', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-='*40)
print(f"Lista de Times do Brasileirão 2018: {times}")
print('-='*40)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-='*40)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('-='*40)
print(f'Os times em ordem alfabética são: \n{sorted(times)}')
print('-='*40)
print(f'O time chapecoense está na {times.index("Chapecoense")+1} posição')
print('-='*40)