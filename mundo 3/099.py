import time
# O * é para desempacotar o paramêtro. Permite atribuir inumeros parametros.
def maior(* num):
    contador = maior = 0
    print('Analisando os valores passados...')
    for v in num:
        contador = contador + 1
        print(f'{v} ', end='', flush=True)
        time.sleep(0.3)
        if contador == 1:
            maior = v
        else:
            if v > maior:
                maior = v
    print(f'Foram informado o total de {len(num)}')
    print(f'O maior valor informado foi {max(num)}')
    print(30 * '-')


maior(2, 1, 7)
maior(5, 4, 7, 9, 2)
maior(1, 4, 7, 20, 2)
maior(0)


