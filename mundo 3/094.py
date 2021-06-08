pessoas = dict()
lista_pessoas = list()
idade = list()
while True:
    pessoas['Nome'] = str(input('Digite seu nome:'))
    while True:
        pessoas['Sexo'] = str(input('Digite seu sexo: [M/F] ')).upper()[0]
        if pessoas['Sexo'] in 'MF':
            break
        print('Digite [M ou F] para o sexo.')
    pessoas['Idade'] = int(input('Digite sua idade: '))
    lista_pessoas.append(pessoas.copy())
    idade.append(pessoas['Idade'])
    parar = str(input('Quer continuar: ')).upper()[0]
    while parar != 'S' and parar != 'N':
        print('Digite sim ou não')
        parar = str(input('Quer continuar: ')).upper()[0]
    if parar == 'N':
        break
#print(lista_pessoas)
print(30 * '=-=')
print(f'Foram cadastradas {len(lista_pessoas)} pessoas')
print('As mulheres cadastradas foram: ', end="")
for p in lista_pessoas:
    for i, s in p.items():
        if s == 'F':
            print(f'{p["Nome"]} ', end="")
print()
media = sum(idade) / len(lista_pessoas)
print(f'A média de idade das pessoas cadastradas foram: {media:5.2f}')
print(30 * '=-=')
print('Lista de pessoas acima da média:')
for p in lista_pessoas:
    for n, i in p.items():
        if p['Idade'] > media:
            print(f' {n} = {i}; ', end="")
            print()
print()
print('Acabou')






