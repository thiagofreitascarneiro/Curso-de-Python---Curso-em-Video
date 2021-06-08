lista = []
contador = 0
nomeVelho = ''
maioridadeM = 0
for c in range(1,5):
    nome = str(input('Digite seu nome:'))
    idade = int(input('Digite sua idade:'))
    sexo = str(input('Digite seu sexo:[M] ou [F]').upper())
    lista.append(idade)
    if c == 1 and sexo == 'M':
        maioridadeM = idade
        nomeVelho = nome
    if idade > maioridadeM and sexo == 'M':
        maioridadeM = idade
        nomeVelho = nome
    if sexo == 'F' and idade < 20:
        contador = contador + 1
print(f'O {nomeVelho} é o homem mais velho e tem {maioridadeM} anos')
print(f'A quantidade de mulheres com menos de 20 anos são de {contador} Mulheres ')
print(f'A média da idade do grupo é {sum(lista)/4}')



