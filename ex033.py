primeiro = float(input('Digite um número: '))
segundo = float(input('Digite outro número: '))
terceiro = float(input('Digite mais um número: '))
maior = primeiro
if segundo > primeiro:
    maior = segundo
if terceiro > maior:
    maior = terceiro
print ('O maior número é: {}'.format(maior))

menor = primeiro
if segundo < primeiro:
    menor = segundo
if terceiro < menor:
    menor = terceiro
print('O menor número é: {}'.format(menor))

