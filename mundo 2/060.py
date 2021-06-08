num = int(input('Digite um número para calcular seu Faotorial:'))
c = num
cont = 0
f = 1
for n in range(1,num):
    cont = cont + 1
    num = num * cont
print(f'O fatorial do número digitado é de {num}')
while c > 0:
    f = f * c
    c = c - 1
print(f'O fatorial do número digitado é de {f}')

