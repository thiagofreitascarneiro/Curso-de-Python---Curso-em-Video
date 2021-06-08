preco = float(input('Qual o preço do produto ? R$'))
desc = (preco/100)*5
total = preco-desc

print(f'O produto que custava R$ {preco}, na pormoção com desconto de 5% vai custar R${total}')