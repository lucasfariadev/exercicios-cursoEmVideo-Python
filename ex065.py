resp = 'S'
quant = soma = media = maior = menor = 0
while resp == 'S':
    n = int(input('Digite um número:'))
    quant +=1
    soma += n
    if quant == 1:
        maior = menor = n
    else:
        if n > n:
            maior = n
        if n < menor:
            menor = n

    resp = str(input('Deseja continuar? [s/n]: ')).strip().upper()[0]
media = soma / quant
print ('A média de valores foi: {}'.format(media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
