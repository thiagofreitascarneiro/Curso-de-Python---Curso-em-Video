import random
import time
def sorteia(lst):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        valor = (random.randint(1, 20))
        lst.append(valor)
        time.sleep(0.3)
        print(f'{valor} ', end='', flush=True)
    print('PRONTO!')


numeros = list()
sorteia(numeros)
print()
def somapar():
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma = soma + i
    print(f'E a soma dos valores Pares são ', end='')
    print(soma)


somapar()


