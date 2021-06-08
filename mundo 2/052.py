print('Vamos verificar se o seu numero é um numero primo')
print(30*'=')
numero = int(input("digite um numero: "))
contador = 0
# + 1 Porque ele sempre conta um a menos dentro do For
for c in range(1, numero + 1):
   if numero % c == 0:
      contador = contador + 1
if contador <=2:
   print(f' o numero {numero} digitado é um numero primo pois ele é divisivel apenas {contador} vezes, ou seja, por 1 e por ele mesmo.')
else:
   print(f'O numero {numero} digitado não é primo pois ele foi divisivel {contador} vezes')








