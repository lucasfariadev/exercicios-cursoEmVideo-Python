from time import sleep
print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
sleep(0.3)
print('Analizando..')
sleep(0.5)
while cont <=10:
    print('{} → '.format(termo), end='')
    termo += razao
    cont +=1
print('FIM')