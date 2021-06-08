num1 = int(input('Escreva um número:'))
num2 = int(input(' Escreve outro número:'))

if num1 > num2:
    print('\033[1;31;30mO primeiro valor é o maior\033[m')

elif num2 > num1:
    print('O segundo valor é o maior')
else:
    print('Os dois valores são iguais')