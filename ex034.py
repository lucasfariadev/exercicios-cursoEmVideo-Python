sal = float(input('Digite o valor do seu salário: '))
if sal > 1250.00:
    print('O seu salário terá um aumento de 10% e passará a ser: R${:.2f} '.format((sal * 0.10) + sal))
else:
    print('O seu salário terá um aumento de 15% e passará a ser: R${:.2f} '.format((sal * 0.15) + sal))
