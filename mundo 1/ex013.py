salario = float(input('Qual o salario do Funcionario ?'))
promocao = (salario/100)*15
total = salario+promocao

print(f'Um funcionário que ganhava R${salario}, com 15% de aumento, passa a receber R${total}')