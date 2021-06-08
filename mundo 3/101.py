def voto(n):
    from datetime import date
    ano = date.today()
    ano = ano.year
    idade = ano - n
    if idade >= 65:
         print(f'Com {idade} anos: VOTO OPOCIONAL')
    elif idade >= 18 and idade < 65:
        print(f'Com {idade} anos: VOTO OBRIGATORIO')
    else:
        print(f'Com {idade} anos: NÃO VOTA')

# Programa Principal
nascimento = int(input('Em que ano você nasceu: '))
voto(nascimento)
