valor = 0
while True:
    print(30 * '_')
    tabuada = int(input('Quer ver a tabuada de qual valor?'))
    print(30 * '_')
    if tabuada < 0:
        break
    for c in range(1,11):
      valor = tabuada * c
      print(f'{tabuada} x {c} = {valor} ')
