larg = float(input('Largura da parede:'))
alt = float(input('Alutura da parede:'))
mQuadrado = (larg*alt)
tintaMetro = mQuadrado/2

print(f'Sua parede tem a dimensão de {larg}x{alt} e sua área é de {mQuadrado}m2.')
print(f'Para pintar essa parede, você precisará de {tintaMetro}l de tinta.')