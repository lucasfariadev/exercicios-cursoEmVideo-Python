def area(b, h):
    a = b * h
    print(f'A área de um terreno de {b}x{h} é de {a}m²')


base = float(input('Qual é o valor da base? '))
altura = float(input('Qual é o valor da altura? '))
area(base, altura)
