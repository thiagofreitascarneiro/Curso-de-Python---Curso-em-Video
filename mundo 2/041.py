from datetime import date
nasc = int(input('Digite o ano de nascimento:'))
categoria = date.today().year - nasc
print(f'\033[1;033;04mVamos analisar sua categoria de acordo com sua idade que é de {categoria} anos\033[m')
if categoria <= 9:
    print('MIRIM')
elif categoria <= 14:
    print('INFANTIL')
elif categoria <= 19:
    print('JUNIOR')
elif categoria <= 20:
    print('SÊNIOR')
else:
    print('MASTER')
