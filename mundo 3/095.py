futebol = dict()
lista_futebol = list()
gols = []
codigo = 0
while True:
    futebol['Nome Jogador'] = str(input('Nome do jogador: '))
    partidas = int(input('Quantas partidas: '))
    for i in range(0, partidas):
        gol = int(input(f'Quantos gols na {i}º partida '))
        gols.append(gol)
    futebol['gols'] = gols[:]
    futebol['TotalGols'] = sum(gols)
    gols.clear()
    futebol['Indice'] = codigo
    codigo = codigo + 1
    lista_futebol.append(futebol.copy())
    continuar = input('Quer continuar: [S/N]').upper()[0]
    print(30 * '===')
    if continuar == "N":
        break
    while continuar != 'S' and continuar != 'N':
        print('Digite corretamente [Sim ou Não]')
        continuar = input('Quer continuar: [S/N]').upper()[0]
print(30 * '=#=')
for i in lista_futebol:
    for n, v in i.items():
        print(f'O campo {n} tem o valor {v}')
    print(30 * '==')
while True:
    indice = int(input('Mostrar indice de qual jogador ? ou Digite 999 pra sair. '))
    if indice == 999:
        break
    if indice >= len(lista_futebol):
        print(f'ERRO! Não existe jogador com o indice {indice}! Tente novamente.')
    # Usei o J para manipular os dados dentro do dicionário
    for j in lista_futebol:
        if indice == j['Indice']:
            print(f'Levantamento do jogador {j["Nome Jogador"]}:')
            for i, v in enumerate(j['gols']):
                print(f'No jogo {i} fez {v} gols.')









