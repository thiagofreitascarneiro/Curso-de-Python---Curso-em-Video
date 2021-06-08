alunos = []
lista = []
contador = 0
maior = []
menor = []
cont = 0
while True:
    alunos.append(str(input('Digite seu nome: ')))
    alunos.append(float(input('digite seu peso: ')))
    lista.append(alunos[:])
    alunos.clear()
    contador = contador + 1
    continuar = str(input('Quer continuar ? ')).upper()[0]
    if continuar == 'N':
        break
print(lista)
print(f'Foram cadastradas o total de {contador} pessoas.')
pesado = []
leve = []
for p in lista:
    cont = cont + 1
    if cont == 1:
        maior = p[1]
        menor = p[1]
    else:
        if p[1] > maior:
            maior = p[1]
        elif p[1] < menor:
            menor = p[1]
for p in lista:
    if p[1] == maior:
        pesado.append(p[0])
    elif p[1] == menor:
        leve.append(p[0])
print(f'O maior peso foi de {maior} KG. Peso de {pesado}.')
print(f'O menor peso foi de {menor} Kg. Peso de {leve}.')