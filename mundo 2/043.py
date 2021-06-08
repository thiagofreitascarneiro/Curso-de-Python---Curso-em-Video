peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura:'))
imc = peso/(altura*altura)
print(f'Seu Imc é {imc}')
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 26:
    print('Peso Ideal')
elif imc > 25 < 31:
    print('Sobrepeso')
elif imc > 30 < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')