soma = 0
for c in range(1,6):
    num = int(input('Digite um numero:'))
    if num % 2 == 0:
        soma = soma + num
print(f'A soma dos numero pares são: {soma}')
