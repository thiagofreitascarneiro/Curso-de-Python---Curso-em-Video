lista = []
valores = []
while True:
    nome = str(input('Digite seu nome: '))
    lista.append(nome)
    nota1 = float(input('Digite sua primeira nota: '))
    lista.append(nota1)
    nota2 = float(input('Digite sua segunda nota: '))
    lista.append(nota2)
    media = (nota1 + nota2)/2
    lista.append(media)
    continuar = input('Quer continuar: [S/N]').upper()[0]
    valores.append(lista[:])
    lista.clear()
    if continuar == 'N':
        break
#print(valores)
for c, i in enumerate(valores):
    print(f'indice {c} O(a) {i[0]} ficou com a média {i[-1]}')
while True:
    mostrar = int(input('Mostrar notas de qual aluno (Digite o indice do aluno que quer ver ou 999 interrompe): '))
    for c, i in enumerate(valores):
        if mostrar == c:
            print(f'Notas de {i[0]} são {i[1:3]}')
    print(40*'=-=')
    if mostrar == 999:
        break

