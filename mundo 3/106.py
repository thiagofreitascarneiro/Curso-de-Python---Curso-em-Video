def manual():

    import time
    cont = 41
    while True:
        if cont > 47:
            cont = 41
        print('\033[32;31;40mSistema de ajuda PyHELP\033[m')
        print(30 * '-')
        menu = str(input(f'\033[30;30;47mFunção da biblioteca > '))
        print(f'\033[28;30;{cont}mAcenssando o manual do {menu}', flush=True)
        time.sleep(0.3)
        print(30 * '-', flush=True)
        x = help(menu)
        print(30 * '-')
        cont = cont + 1
        if menu == 'fim':
            print('\033[32;33;41m Até Logo!')
            break


manual()