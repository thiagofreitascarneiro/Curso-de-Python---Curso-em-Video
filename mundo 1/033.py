valor1 = int(input('Primeiro valor:'))
valor2 = int(input('Segundo valor:'))
valor3 = int(input('Terceiro Valor:'))
#verificando quem é o menor
if valor1 < valor2 and valor1 < valor3:
    print(f'O menor valor digitado foi: {valor1}')
if valor2 < valor1 and valor2 < valor3:
    print(f'O menor valor digitado foi: {valor2}')
if valor3 < valor1 and valor3 <valor2:
    print(f'O menor valor digitado foi: {valor3}')

#verificando quem é o maior
if valor1 > valor2 and valor1 > valor3:
    print(f'O maior valor digitado foi: {valor1}')
if valor2 > valor1 and valor2 > valor3:
    print(f'O maior valor digitado foi: {valor2}')
if valor3 > valor1 and valor3 > valor2:
    print(f'O maior valor digitado foi: {valor3}')






