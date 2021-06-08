print('Progressão aritimética')
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da P.A: '))
cont = 1
qtdtermo = 10
while cont <= qtdtermo and qtdtermo != 0:
    print(f'{termo} >', end=" ")
    termo = termo + razao
    cont = cont + 1
    if cont > qtdtermo:
        cont = 1
        print(f'{termo} >', end=" ")
        termo = termo + razao
        cont = cont + 1
        qtdtermo = int(input('você quer ver mais termos ? se sim, digite a quantidade que quer ver ou digite 0 pra sair: '))




