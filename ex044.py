preco = float(input('\033[1;30;41mPreço das compras:\033[m \033[32mR$\033[m'))
print('''\033[34mFORMAS DE PAGAMENTO\033[m
\033[1;31m[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão\033[m''')
opcao = int(input('\033[1;33mQual é a opção?\033[m '))
if opcao == 1:
    print('Sua compra de {} vai custar {} no final'.format(preco, preco - (preco*0.1)))
elif opcao == 2:
    print('Sua compra de {} vai custar {} no final'.format(preco, preco - (preco*0.05)))
elif opcao == 3:
    print('sua compra de {} será parcelada em 2x sem juros de R${:.2f}'.format(preco, preco / 2))
elif opcao == 4:
    par = int(input('\033[1;33mQuantas parcelas?\033[m '))
    print('sua compra será parcelada em \033[4;35m{}x\033[m de \033[4;35mR${:.2f}\033[m COM JUROS'.format(par, (preco +(preco*0.2)/ par)))
    print('Sua compra de \033[1;33mR${}\033[m vai custar \033[1;33mR${}\033[m no final.'.format(preco, preco + (preco*0.2)))
else:
    print('\033[7;34;42mOpção inválida! Tente novamente\033[m')