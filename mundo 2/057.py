sexo = 'R'
while sexo != 'M' and sexo != 'F':
  sexo = str(input('Digite seu sexo: [M] ou [F]: ')).upper().strip()[0]
print(f'Sexo {sexo} registrado com sucesso!')


