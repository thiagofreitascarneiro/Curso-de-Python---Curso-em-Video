import random
n1 = str(input('Primeiro Aluno'))
n2 = str(input('Segundo Aluno'))
n3 = str(input('Terceiro Aluno'))
n4 = str(input('Quarto Aluno'))
lista = [n1,n2,n3,n4]
Ordem = random.sample(lista,k=4)

print(f'A ordem de apresentação será: {Ordem}')