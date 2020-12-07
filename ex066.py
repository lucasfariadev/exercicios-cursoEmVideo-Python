n = tot = soma = 0
while True:
        n = int(input('Digite um número: '))
        if n == 999:
            break
        tot +=1
        soma += n
print(f'você digitou {tot} números e soma entre eles foi {soma}')
