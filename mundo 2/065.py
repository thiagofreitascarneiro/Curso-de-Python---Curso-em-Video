num = int(input('Digite um valor: ou digite 99 para Sair '))
soma = 0
contador = 0
maior = num
menor = num
while num != 99:
    soma = soma + num
    num = int(input('Digite um valor: ou digite 99 para Sair '))
    if num > maior and num != 99:
        maior = num
    if num < maior and num != 99:
        menor = num
    contador = contador + 1
    if contador >= 2 and num != 99:
        contador = contador + 1
        soma = soma + num
        num = int(input('Quer continuar a digitar valores: Se não quiser, digite 99 '))
    if num > maior and num != 99:
        maior = num
    if num < maior and num != 99:
        menor = num
print(f'o maior valor é {maior} , o menor é {menor}, a média dos valores lidos são {soma/contador}')

