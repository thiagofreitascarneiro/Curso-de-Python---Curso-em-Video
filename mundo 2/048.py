valor = 0
cont = 0
for s in range(1,501,2):
    if s % 3 == 0:
        valor = valor + s
        cont = cont + 1
print(f'O valor total de todos os {cont} números Multiplos de 3 é {valor}')





