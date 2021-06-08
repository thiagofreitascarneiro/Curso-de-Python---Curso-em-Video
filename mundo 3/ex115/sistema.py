from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
   criarArquivo(arq)


while True:
    resp = menu(['Lista de pessoas cadastradas', 'cadastrar novo usuario', 'Sair'])
    if resp == 1:
        # opção de listar um conteudo com arquivo.
        lerArquivo(arq)
    elif resp == 2:
        # opção de cadastrart nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resp == 3:
        print('Saindo....')
        sleep(1)
        print('\033[32mObrigado! Volte sempre.\033[m')
        break
    else:
        print('\033[31mERRO! Digite uma opção valida!\033[m')
    sleep(2)
