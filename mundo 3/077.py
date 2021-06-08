palavras = ('aprender', 'programar', 'gratis',
            'mercado', 'python', 'futuro',
            'biblioteca')
cont = 0
for p in palavras:
    print(f'\nNa palavra {p} temos ', end = '')
    for v in p:
        if v in 'aeiou':
            print(v, end=' ')

