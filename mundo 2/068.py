from random import randint
print('Vamos jogar par ou impar :) ')
while True:
    computador = randint(1, 10)
    num = int(input('digite um valor: '))
    valor = (computador + num)%2
    parImpar = str(input('Par ou impar? [P/I]')).upper()[0]
    if parImpar == 'P' and valor == 0:
        print(f'Você jogou {num} e o computador jogou {computador}. Total de {num + computador} DEU PAR.')
        print(30 * '-')
        print('Você VENCEU!!!')
        print(30 * '-')
        print('Vamos jogar novamente...')
        print(30 * '-')
    if parImpar == 'I' and valor == 1:
        print(f'Você jogou {num} e o computador jogou {computador}. Total de {num + computador} DEU IMPAR.')
        print(30 * '-')
        print('Você VENCEU!!!')
        print(30 * '-')
        print('Vamos jogar novamente...')
        print(30 * '-')
    if valor == 0 and parImpar == 'I':
        print(f'Você jogou {num} e o computador jogou {computador}. Total de {num + computador} DEU PAR.')
        print(30 * '-')
        print('Você PERDEU!!!')
        print(30 * '-')
        break
    if valor == 1 and parImpar == 'P':
        print(f'Você jogou {num} e o computador jogou {computador}. Total de {num + computador} DEU IMPAR.')
        print(30 * '-')
        print('Você PERDEU!!!')
        print(30 * '-')
        break
