valor = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual o seu Salario: R$'))
ano = int(input('Quantos anos sera financiado: R$'))
prestacao = valor/(ano * 12)

print(f'Para pagar uma casa de {valor} em {ano}')
print(f'A prestação sera de {prestacao}')

if prestacao > (salario*30)/100:
    print('empréstimo negado!')
elif prestacao <= (salario*30)/100:
    print('\033[1;31;43mempréstimo aprovado!\033[m')