print('Lojas CARNEIRO')
print(40 * '-')
total = contador = produtoBarato = marcador = 0
menor = ' '
while True:
    continuar = ' '
    nome = str(input('Nome do produto: '))
    valor = float(input('Valor do produto: R$ '))
    marcador = marcador + 1
    total = total + valor
    if marcador == 1:
        produtoBarato = valor
        menor = nome
    if marcador > 1 and valor < produtoBarato:
        produtoBarato = valor
        menor = nome
    if valor > 1000:
        contador = contador + 1
    while continuar not in 'SN':
        continuar = str(input('Você deseja continuar [S/N] ?')).upper()[0]
    print(40 * '-')
    if continuar == 'N':
        break
print(f'O total gasto na compra foi de {total}')
print(f'Os produtos com o valor acima de 1000,00 R$ foi de {contador} produtos')
print(f'O produto mais barato foi o/a {menor} que custa {produtoBarato} R$')


