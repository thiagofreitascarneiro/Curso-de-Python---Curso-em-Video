from datetime import date
sexo = str(input('Qual o seu sexo: (Digite M(masculino ou F(feminino)'))
ano = int(input('Qual o ano do seu nascimento:'))
alistamento = date.today().year - ano
if sexo == 'F':
   print('Seu sexo não exige alistamento')
elif alistamento == 17 and sexo == 'M':
   print('É a hora de se alistar.')
elif alistamento <= 17 and sexo == 'M':
    print(f'Ainda não chegou a hora de se alistar ao serviço militar, faltam {17 - alistamento} anos')
elif alistamento > 17 and sexo == 'M':
    print(f'\033[1;0;042mjá passou {alistamento - 17} anos do alistamento.\033[m')
