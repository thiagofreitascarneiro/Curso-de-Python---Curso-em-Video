nota1 = float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite sua segunda nota:'))
media = (nota1 + nota2)/2
print(f'\033[1;33;43msua média é {media}\033[m')
if media <= 5.0:
    print('REPORVADO!')
elif  media > 5.0 and media < 7.0:
    print('RECUPERAÇÃO')
else:
    print('APROVADO!')

