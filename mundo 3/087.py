matriz = [[], [], []]
valores_pares = []
terceira_coluna = []
teste = []
for l in range(0, 3):
        for c in range(0, 3):
            matriz[l].append(int(input(f"Digite um valor para [{l},{c}]: ")))
print('-=' * 30)
for l in range(0, 3):
        for c in range(0, 3):
                print(f'[{matriz[l][c]:^5}]', end='')
        print()
for i in matriz[0]:
    if i % 2 == 0:
        valores_pares.append(i)
for i in matriz[1]:
    if i % 2 == 0:
        valores_pares.append(i)
for i in matriz[2]:
    if i % 2 == 0:
        valores_pares.append(i)
terceira_coluna.append(matriz[0][2])
terceira_coluna.append(matriz[1][2])
terceira_coluna.append(matriz[2][2])
print(matriz)
print('-=' * 30)
print(valores_pares)
print(f'O maior valor da segunda linha é {max(matriz[1])}')
print(f'A soma dos valores Pares é {sum(valores_pares)}')
print(f'A soma dos valores da terceira coluna é {sum(terceira_coluna)}')


