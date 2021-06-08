valores = []
maior = menor = indice = indice2 = quant = 0
for i in range(0, 5):
    valores.append((int(input(f'Digite um Valor para a posição {i}: '))))
    quant = quant + 1
    if quant == 1:
        maior = valores[i]
        menor = valores[i]
    else:
        if valores[i] > maior:
            maior = valores[i]

        if valores[i] < menor:
            menor = valores[i]
print(f'Você digitou os valores {valores}')
print(40 * '==')
print(f"O maior valor digitado foi {maior}   ", end = '')
for i, v in enumerate(valores):
    if v == maior:
        print(f' na posição {i}...', end='')
print('')
print(f'O menor valor digitado foi {menor}  ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f' na posição {i}...', end="")












