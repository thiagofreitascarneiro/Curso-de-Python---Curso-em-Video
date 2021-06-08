valor = []
while True:
    valor.append(int(input('Digite um valor :')))
    resp = str(input('Você quer continuar digitando:[S/N]')).upper()[0]
    if resp == 'N':
        break
print(40 * '=-=')
for c, v in enumerate(valor):
    if 5 == v:
        print(f'O valor 5 está na lista na posição {c}.')
if 5 not in valor:
    print(f'O valor 5 não esta na lista')
print(f'Foram digitados o total de {len(valor)} valores')
valor.sort(reverse=True)
print(f'lista de forma decrescente {valor}')

