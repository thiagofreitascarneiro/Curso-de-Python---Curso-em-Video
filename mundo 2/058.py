from random import randint
sorteia = randint(0, 10)
numero = -1
contador = 0
print('Vamos jogar! vou pensar em numero e você tenta adivilha-lo:')
while sorteia != numero:
    numero = int(input('Digite um numero de 0 a 10: '))
    contador = contador + 1
    if numero > sorteia:
        print('Menos... Tente mais uma vez.')
    elif numero < sorteia:
        print('Mais... Tente mais uma vez.')
print(f'O numero pensado foi {sorteia} e você precisou de {contador} tentativas para acertar')