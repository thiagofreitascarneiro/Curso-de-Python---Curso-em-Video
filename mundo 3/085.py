lista = [[], []]
for i in range(0, 7):
    numero = (int(input(f'Digite o {i + 1}º valor: ')))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
print(f'Os numeros pares são: {sorted(lista[0])}')
print(f'Os numeros impares são: {sorted(lista[1])}')

