def leiaint(num):
    valor = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('\033[32;32;40mERRO! Digite um número inteiro:\033[m')
    return valor


n = leiaint('Digite um número Inteiro: ')
print(f'\033[0;30;42mO valor inteiro digitado foi {n}\033[m')



