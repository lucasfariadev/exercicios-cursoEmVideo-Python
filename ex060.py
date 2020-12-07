#from math import factorial
#n1 = int(input('Digite um número para calcular o Fatorial: '))
#f = factorial(n1)
#print('O fatorial de {} é {}'.format(n1, f))
n1 = int(input('Digite um número para calcular o Fatorial: '))
c = n1
f = 1
print('Cauculando {}! = '.format(n1), end='')
while c > 0:
    print(' {}'.format(c), end='')
    print(' x'if c>1 else ' =', end=' ')
    f *= c
    c -= 1
print('{}'.format(f))
