tabela = dict()
tabela['nome'] = str(input('Digite seu nome: '))
tabela['media'] = float(input(f'A Média de {tabela["nome"]}: '))
if tabela["media"] >= 7:
    tabela['situacao'] = 'Aprovado'
else:
    tabela['situacao'] = 'Reprovado'
for k, v in tabela.items():
    print(f'{k} é igual a {v}')
