seg1 = float(input('Primeiro segmento:'))
seg2 = float(input('Segundo segmento:'))
seg3 = float(input('Terceiro Segmento:'))
print('\033[1;33;04m Verificando os segmentos do seu triangulo...\033[m ')
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 +seg2:
    print('\033[1;30;45mOs segmentos acima PODEM FORMAR um Triângulo\033[m')
    if seg1 == seg2 and seg1 == seg3 and seg2 == seg3:
        print('\033[1;30;45m É um triangulo EQUILATERO! \033[m')
    elif seg1 != seg2 and seg2 != seg3 and seg3 != seg1:
            print('\033[1;30;43m É um triangulo ESCALENO! \033[m')
    else:
        print('\033[1;36;40m É um triângulo ISÓSCELES!\033[m')
else:
    print('Os segmentos não podem Formar um triângulo.')
