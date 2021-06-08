from math import sin, cos, tan, radians
Ângulo = float(input('Digite o ângulo que você deseja: '))
Seno = sin(radians(Ângulo))
Cosseno = cos(radians(Ângulo))
Tangente = tan(radians(Ângulo))
print(f'O ângulo de {Ângulo} tem o seno de {Seno:.2f}.')
print(f'O ângulo de {Ângulo} tem o cosseno de {Cosseno:.2f}.')
print(f'O ângulo de {Ângulo} tem o tangente de {Tangente:.2f}.')