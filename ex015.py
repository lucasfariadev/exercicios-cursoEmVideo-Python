d = int(input('Informe quantos dias ficou com o carro: '))
km = float(input('Digite quantos km foram rodados: '))
vkm = km * 0.15
vd = d * 60
print('O valor a pagar pelo aluguel por {}km rodados e {}dia(s) é de R${:.2f}'.format(km, d, vkm + vd))