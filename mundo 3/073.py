times = ('Flamengo', 'Internacional', 'Atletico MG','Sao Paulo', 'Fluminense',
         'Gremio', 'Palmeiras', 'Santos', 'Athletico PR','Bragantino',
         'Ceara', 'Corinthians', 'Atletico GO', 'Bahia', 'Sport', 'Fortaleza',
         'Vasco', 'Goias', 'Coritiba', 'Botafogo')
print('Campeonato Brasileiro 2020')
print(40 *'=')
print(f'Os 5 primeiros colocados são {times[0:5]}')
print(40 *'=')
print(f'Os 4 ultimos times da tabela são {times[16:20]}')
print(40 *'=')
print(f'Lista do time em ordem alfabética {sorted(times)}')
print(40 *'=')
print(f'O Brgantino está na {times.index("Bragantino") + 1}º posição .')
for c in range(10,11):
    print(f'O {times[c]} está na {c + 1}º posição .')
