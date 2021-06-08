def fatorial(num, show=False):
    '''
    :param num: O número a ser calculado
    :param show: (opicional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um numemro num.
    '''
    resultado = fator = contador = 0
    valor = num - 1
    while valor != 0:
        contador = contador + 1
        if contador == 1:
            fator = (num * valor)
            resultado = resultado + fator
        else:
            fator = resultado * valor
            resultado = fator
        valor = valor - 1
    if show:
        for i in range(num, 0, -1):
            if i > 1:
                print(f'{i} x ', end='')
            elif i == 1:
                print(f'{i} = ', end='')
    return resultado


help(fatorial)
print(fatorial(5, True))
