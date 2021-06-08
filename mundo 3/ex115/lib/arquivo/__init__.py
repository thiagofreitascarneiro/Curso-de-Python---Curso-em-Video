from ex115.lib.interface import *
def arquivoExiste(nome):
    try:
        # rt significa read text
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        #wt significa write text e o + é para criar o arquivo caso ele não exista
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
       a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de preencher os dados!')
        else:
            print(f'Novo registro de \033[36m{nome}\033[m cadastrado com sucesso.')
            a.close()
