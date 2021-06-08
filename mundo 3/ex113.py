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


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[33mERRO: por favor, digite um número Real válido.\033[m')
            # o continue serve para jogar o valor n para o While novamente.
            continue
        except (KeyboardInterrupt):
            print('\033[35mO usuario preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n



n1 = leiaInt('Digite um valor Inteiro: ')
n2 = leiaFloat('Digite um valor Real: ')
print(f'O valor inteiro digitado foi {n1} e o Real foi {n2}')