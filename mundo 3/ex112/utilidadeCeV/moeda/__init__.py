def aumentar(v=0, i=0, formato=False):
    valor = (v * i)/100
    valor = valor + v
    return valor if formato is False else moeda(valor)


def metade(v=0, formato=False):
    valor = v/2
    return valor if formato is False else moeda(valor)


def dobro(v=0, formato=True):
    valor = v * 2
    return valor if formato is False else moeda(valor)


def diminuir(v=0, i=0, formato=False):
    valor = (v * i)/100
    valor = v - valor
    return valor if formato is False else moeda(valor)


def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:>.2f}'.replace('.', ',')


def resumo(valor, aumento, reducao):
    print(30 * '-')
    resumo = 'RESUMO VALOR'
    print(f'{resumo:>20}')
    print(30 * '-')
    print(f'Preço analisado:\t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor,True)}')
    print(f'Metade do preço:\t{metade(valor,True)}')
    print(f'80% de aumento: \t{aumentar(valor, aumento, True)}')
    print(f'35% de redução: \t{diminuir(valor, aumento, True)}')
    print(30 * '-')