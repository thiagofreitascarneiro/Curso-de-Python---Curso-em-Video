import random
aluno1 = str(input('Primeiro Aluno:'))
aluno2 = str(input('Segundo aluno:'))
aluno3 = str(input('Terceiro aluno:'))
aluno4 = str(input('Quarto aluno:'))
lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.choice(lista)

print(f'O aluno sorteado foi {sorteio}')