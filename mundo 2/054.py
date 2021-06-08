from datetime import date
print('\033[1;32;01mVamos Verificar se vocês já atingiram a maioridade.\033[m')
print(30*'\033[1;33;01m=*=\033[m')
hoje = date.today().year
contador1 = 0
contador2 = 0
for c in range(1,8):
    ano = int(input('Digite o ano de nascimento:'))
    if hoje - ano >= 18:
        contador1 = contador1 + 1
    else:
        contador2 = contador2 + 1
print(f'\033[1;34;02m{contador1} pessoas já atingiram a maioridade.\033[m')
print(f'\033[1;35;03m{contador2} pessoas não atingiram a maioridade\033[m')