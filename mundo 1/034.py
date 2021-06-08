salario = float(input('Qual é o salario do funcionario:'))

if salario > 5000:
    aumento = (salario/100)*10 + salario
    print(f'Quem ganhava {salario} passa a ganhar {aumento}')
else:
    aumento = (salario/100)*15 + salario
    print(f'Quem ganahava {salario} passa a ganhar {aumento}')