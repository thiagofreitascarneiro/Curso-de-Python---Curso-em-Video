soma = 0
contador = 0
while True:
    num = int(input("digite um numero qualquer ou digite 999 para sair : "))
    if num == 999:
        break
    soma = num + soma
    contador = contador + 1
print(f'você digitou {contador} numeros e a soma deles foi de {soma}')
