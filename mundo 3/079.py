lista = []
continuar = 'S'
while continuar == 'S':
        valor = (int(input(f'Digite um valor: ')))
        if valor not in lista:
            lista.append(valor)
        else:
            print('Valor Duplicado! Não vou adicionar...')
        continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
print(f'Você digitou {sorted(lista)}')







