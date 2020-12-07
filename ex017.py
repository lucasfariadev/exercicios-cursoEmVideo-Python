from math import hypot
n = ('-')
print('{}ex 017{}'.format(n*6, n*6))
print('Crie um programa que leia o número\ndo comprimento do cateto oposto e do cateto adjascente\nde um triangulo retângulo. Calcule e mostre a hipotenusa')
co = float(input('cateto oposto: '))
ca = float(input('cateto adjascente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))


