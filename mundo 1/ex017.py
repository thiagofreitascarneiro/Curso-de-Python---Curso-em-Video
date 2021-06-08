import math
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hipot = math.hypot(co, ca)
print(f'A hipotenusa vai medir {hipot:.2}')


