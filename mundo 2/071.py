print('------Caixa Eletrônico-------')
print(40*'-')
valor = int(input('Qual o valor a ser sacado :'))
total = valor
cedulas = 50
totced = 0
while True:
    if total >= cedulas:
        total = total - cedulas
        totced = totced + 1
    else:
        print(f'Total de {totced} cédulas de {cedulas} R$')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        totced = 0
        if total == 0:
            break
print(40 * '=')
print('Volte sempre. Banco dos Carneiros')