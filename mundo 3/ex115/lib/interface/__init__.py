def linha(tam = 42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[34m{c}\033[m - \033[33m{item}\033[m')
        c = c + 1
    print(linha())
    opc = leiaInt('\033[36mSua opção:\033[m')
    return opc


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[33mERRO: por favor, digite um número inteiro válido.\033[m')
            # o continue serve para jogar o valor n para o While novamente.
            continue
        except (KeyboardInterrupt):
            print('\033[35mO usuario preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n



















