valores = []
while True:
    valores.append(int(input('Digite um valor:')))
    resp = str(input('Quer continuar: ')).upper()[0]
    if resp == 'N':
        break
pares = []
impares = []
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Os valores digitados foram {valores}')
print(f'Os valores pares foram {pares}')
print(f'Os valores impares foram {impares}')
