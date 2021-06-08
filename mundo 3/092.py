import datetime
print('Carteira de Trabalho')
print(40*'-=-')
carteira = dict()
carteira['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
ano = datetime.date.today().year
idade = ano - nascimento
carteira['idade'] = idade
carteira['carteira Trabalho'] = int(input('Carteira de trabalho (0 não tem): '))
if carteira['carteira Trabalho'] != 0:
    carteira['ano do contrato'] = int(input('Ano de contratação: '))
    carteira['salario'] = float(input('Salário: R$ '))
    aposentar = carteira['ano do contrato'] - nascimento
    carteira['Aposentadoria'] = aposentar + 35
print(carteira)
print(40*'-=-')
for c, i in carteira.items():
    print(f'{c} tem o valor {i}')
print(40*'-=-')

