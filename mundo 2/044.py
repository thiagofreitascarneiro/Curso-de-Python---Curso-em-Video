preco = float(input('Qual o preço do produto ?'))
pagamento = float(input('''Quantas parcelas:
        [1] a Vista
        [2] a Vista no Cartão
        [3] 2x no Cartão
        [4] 3x ou mais
         '''))
if pagamento == 1:
    desc = ((preco * 10)/100)
    print(f'O valor da sua compra é R${preco}, o desconto será de R${desc} valor total de R${preco - desc}')
elif pagamento == 2:
    desc =((preco * 5)/100)
    print(f'O valor da sua compra é R${preco}, o desconto será de R${desc} valor total de R${preco - desc} ')
elif pagamento == 3:
    print(f'Sua compra será parcelada em R${pagamento}x de R${preco/pagamento} com total de R${preco}')
elif pagamento == 4:
    juros = (preco*20)/100
    print(f'O valsor total da compra é R${preco} sera parcelada em R${pagamento}x de R${(preco*juros)/pagamento} parcelas com total de R${preco + juros}')
else:
    print('Opção invalida de pagamento. Tente novamente!')