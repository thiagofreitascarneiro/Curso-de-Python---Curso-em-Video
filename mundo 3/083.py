valor = str(input('Digite uma expressão: '))
quant_Abrir = valor.count('(')
quant_Fechar = valor.count(')')
print(quant_Fechar)
print(quant_Abrir)
if quant_Fechar % 2 == 0 and quant_Abrir % 2 == 0:
    print('Essa expressão está correta!')
else:
    print('essa expressão esta Equivocada!')


