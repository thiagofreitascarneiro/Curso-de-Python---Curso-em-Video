num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
resultado = 0
programa = False
menu = int(input('''MENU
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA
: '''))
while not programa:
    if menu == 1:
        resultado = num1 + num2
        programa = True
    elif menu == 2:
        resultado = num1 * num2
        programa = True
    elif menu == 3:
        if num1 > num2:
            resultado = num1
            programa = True
        else:
            resultado = num2
            programa = True
    elif menu == 4:
        programa = False
        print('Digite os numeros Novamente. ')
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        menu = int(input('''MENU
        [1] SOMAR
        [2] MULTIPLICAR
        [3] MAIOR
        [4] NOVOS NUMEROS
        [5] SAIR DO PROGRAMA
        : '''))
    elif menu == 5:
        programa = True
    elif menu > 5:
        programa = False
        print('oção invalida. Digite novamente.')
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        menu = int(input('''MENU
                [1] SOMAR
                [2] MULTIPLICAR
                [3] MAIOR
                [4] NOVOS NUMEROS
                [5] SAIR DO PROGRAMA
                : '''))
print(f'você escolheu a opção {menu}, portanto o resultado foi de {resultado}.')
