print('Progressão aritmética')
print(10*'_*_')
termo = int(input('Digite o primeiro Termo '))
razao = int(input('Digite a razão de uma P.A '))
print('Os 10 primeiros termos da progressão aritmética são:')
for c in range(1,11):
    print(f'{termo}')
    termo = termo + razao
print('Acabou')
