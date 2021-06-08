import time
def contador(inicio, fim, passo):
    print('-' * 30)
    print(f'A contagem de {inicio} até {fim}  de {passo} em {passo}')
    if inicio < fim:
        for n in range(inicio, fim + 1, passo):
            time.sleep(0.3)
            print(n, end=' ')
    if inicio >= fim:
        for n in range(inicio, fim - 1, passo):
            time.sleep(0.3)
            print(n, end=' ')
    elif fim < 0:
        for n in range(inicio, fim + 1, passo):
            time.sleep(0.3)
            print(n, end=' ')



contador(1, 10, 1)
contador(10, 0, -2)
print('-' * 30)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if passo == 0:
    passo = 1

contador(inicio, fim, passo)
