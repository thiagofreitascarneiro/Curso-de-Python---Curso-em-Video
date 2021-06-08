futebol = dict()
futebol['Nome Jogador'] = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidas: '))
gols = []
for i in range(0, partidas):
    gol = int(input(f'Quantos gols na {i}º partida '))
    gols.append(gol)
futebol['gols'] = gols[:]
futebol['TotalGols'] = sum(gols)
print(futebol)
print(30 * '=#=')
for n, i in futebol.items():
    print(f'O campo {n} tem o valor {i}')
print(30 * '=#=')
print(f'O jogador {futebol["Nome Jogador"]} jogou {partidas} partidas')
for i, v in enumerate(futebol['gols']):
    print(f'Na partida {i}, fez {v} gols')
print(f'Foi um total de {futebol["TotalGols"]}')