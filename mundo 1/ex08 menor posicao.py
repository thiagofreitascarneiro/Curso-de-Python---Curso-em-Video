def menorpos(numeros):
    cont = menor = pos = 0
    for c, i in enumerate(numeros):
        cont = cont + 1
        if cont == 1:
            menor = i
            pos = c
        else:
            if i < menor:
                menor = i
                pos = c
    return pos


v = [3, 5, 1, 30, 50, 100]
print(menorpos(v))



