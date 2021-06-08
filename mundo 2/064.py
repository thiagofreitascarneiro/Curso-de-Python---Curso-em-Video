n = 0
contador = 0
valor = []
while n != 999:
    n = int(input('''Digite um numero qualquer:
        Se quiser sair, digite 999
    '''))
    if n != 999:
        valor.append(n)
    contador = contador + 1
    if n == 999:
     contador = contador - 1
print(f'Você digitou {contador} e a soma deles foi {sum(valor)}')
