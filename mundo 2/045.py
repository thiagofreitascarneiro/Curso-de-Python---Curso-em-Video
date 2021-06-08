from random import randint
print('Vamos jogar JOKENPÔ ?')
itens = ('Pedra', 'Papel', 'Tesoura')
jogador = int(input('''Selecione sua opção abaixo:
[0] PEDRA
[1] PAPEL
[2] TESOURA
'''))
sorteia = randint(0,2)
print(f'O computador escolheu {itens[sorteia]}')
print(f'Você escolheu {itens[jogador]}')
if jogador == 0:
    if sorteia == 0:
         print('Empatou, Jogue novamente.')
    elif sorteia == 1:
         print('Você Perdeu')
    elif sorteia == 2:
        print(f'Você Ganhou')
elif jogador == 1 :
    if sorteia == 0:
        print('Você venceu')
    elif sorteia == 1:
        print('Empatou, Jogue novamente.')
    elif sorteia == 2:
        print(f'Computador venceu')
elif jogador == 2:
    if sorteia == 0:
        print('Computador Venceu')
    elif sorteia == 1:
        print('Você Ganhou')
    elif sorteia == 2:
        print('Empatou, Jogue novamente.')
else:
    print('Opção invalida')




