from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa',  'Sair do Sistema'])
    if resposta == 1:
        #Opção de listar o conteudo de um arquivo:
        lerArquivo('cursoemvideo.txt')
        sleep(1)
    elif resposta == 2:
        #opção de cadastrar uma nova pessoa:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        # opção de sair do sistema
        sleep(0.5)
        cabeçalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
    sleep(2)