lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
         'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90 )
print('LISTAGEM DE PREÇOS')
print(40 * '=')
for itens in range(0, len(lista),2):
    print(f'{lista[itens]} {15 * "."} R$ {"%.2f" % lista[itens + 1]}', end=" ")
    print(" ")
print(40 * '=')

