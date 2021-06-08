aluguel = int(input('Quantidade de dias alugado:'))
km = int(input('Quantidade de Km percorrido ?'))
custoAluguel = 60
custoKm = 0.15
valorAluguel = aluguel*custoAluguel
valorKm = custoKm*km

print(f'Valor do aluguél é de {valorAluguel}, o valor do Km rodado é de {valorKm} e o total a pagar é de {valorAluguel+valorKm}')