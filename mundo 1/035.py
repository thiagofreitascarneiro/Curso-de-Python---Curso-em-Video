seg1 = float(input('Primeiro segmento:'))
seg2 = float(input('Segundo segmento:'))
seg3 = float(input('Terceiro Segmento:'))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 +seg2:
    print('\033[1;30;45mOs segmentos acima PODEM FORMAR Triângulo\033[m')
else:
    print('\033[1;36;40mNão podem formar triângulo\033[m')
