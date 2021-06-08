valores = (int(input('Digite 4 valores: ')),
          int(input('Digite 4 valores: ')),
          int(input('Digite 4 valores: ')),
          int(input('Digite 4 valores: ')))
print(f'O numero 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O numero 3 apareceu na {valores.index(3) + 1}º posição.')
else:
    print(f'O numero 3 não apareceu em nenhum valor digitado')
for n in valores:
    if n % 2 == 0:
        print(n, end= " ")





