lista = []
for i in range(0, 5):
    valor = (int(input('Digite 5 numeros: ')))
    if i == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print(f'Adicionado na posição {pos}')
                break
            pos = pos + 1
print(40 * '==')
print(f'Os valores digitados em ordem foram {lista}')



