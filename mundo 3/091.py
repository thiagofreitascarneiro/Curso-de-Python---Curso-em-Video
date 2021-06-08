from random import randint
from time import sleep
from operator import itemgetter
jogador = {}
cont = 0
print('Valores Sorteados:')
for i in range(1, 5):
    jogador[i] = randint(1, 6)
for j, d in jogador.items():
    sleep(1)
    print(f'O Jogador{j} tirou {d}')
print('Ranking dos jogadores:')
print(jogador)
#Serve para ordenar um dicionario do maior para o menor
ranking = list()
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i, v in enumerate(ranking):
    print(f'O jogador{v[0]} ficou na posição {i + 1}º com {v[1]}')
    sleep(1)






