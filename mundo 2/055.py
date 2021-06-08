print('Vamos calcular o maior e o menor Peso digitado de 5 pessoas')
lista = []
for p in range(1,6):
    peso = float(input(f'Digite o peso:'))
    lista.append(peso)
print(f'O peso maximo foi de {max(lista)} KG')
print(f'O peso minimo foi de {min(lista)} KG')