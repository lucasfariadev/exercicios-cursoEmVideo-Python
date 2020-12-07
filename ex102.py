def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um numero
    :param n: numero a ser calculado
    :param show: mostrar ou não a conta(opicional
    :return: o valor do fatorial do numero n
    """
    f=1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print('=', end='')
        f *= c
    return f


print(fatorial(5, show=True))