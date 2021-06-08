numero = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
valor = int(input('Digite um número entre 0 e 20: '))
extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while valor not in numero:
    valor = int(input('Digite um número entre 0 e 20: '))
print(f'você digitou o número {extenso[valor]}')

