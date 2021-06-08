from random import randint
from time import sleep
numero = randint(0,5)
print('_=_'*20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('_=_'*20)
palpite = int(input('em que numero eu pensei ?'))
print('PROCESSANDO...')
sleep(3)
if palpite == numero:
    print('PARÁBENS! você acertou.')
else:
    print(f'GANHEI! eu pensei no numero {numero} e não no {palpite}')