distancia = int(input('Digite a distância da sua viagem em Km:'))

if distancia <=200:
    valor = distancia * 0.50
    print(f'O preço da passagem para {distancia} Km é de {valor} R$')
else:
    valor = distancia * 0.45
    print(f'O preço da passagem para {distancia}Km é de {valor} R$')