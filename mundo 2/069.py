homens = maioridade = mulheres = 0
continuar = 'S'
while continuar == 'S':
    sexo = ' '
    print('CADASTRE UMA PESSOA')
    while sexo not in 'FM':
        print(30 * '-')
        print('CADASTRE UMA PESSOA')
        sexo = str(input('Digite seu sexo: [M/F] ')).upper()[0]
    idade = int(input('Digite sua idade: '))
    if idade > 18:
        maioridade = maioridade + 1
    if sexo == 'M':
        homens = homens + 1
    if sexo == 'F' and idade < 20:
        mulheres = mulheres + 1
    if continuar == "N":
        break
    if continuar == "S":
        continuar = str(input('Quer continuar: ')).upper()[0]
print(f'Total de pessoas com mais de 18 ano: {maioridade}')
print(f'Ao todo temos {homens} Homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')
