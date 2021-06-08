import time
from random import sample
print(40 * '=-=')
print('MEGA SENA DA VIRADA')
print(40 * '=-=')
sorteia = []
jogos = int(input('Quantos jogos você quer que eu sorteie: '))
print(40 * '=-=')
print(f'=-=-=-=-=-=-=VAMOS SORTEAR {jogos} Jogos!=-=-=-=-=-=')
for i in range(0, jogos):
    sorteia.append(sample(range(1, 60), 6))
    time.sleep(1)
    print(f'Jogo {i + 1}: {sorteia[i]}')
print(40 * '=-=')
print('=-=-=-=-=-=-=BOA SORTE!=-=-=-=-=-=')
print(40 * '=-=')




