print('Vamos testar se a frase é um palíndromo')
print(30*'*_*')
frase = str(input('Digite uma frase:'))
frase = frase.replace(" ","")
# começo do inicio e termino no fim :: de trás pra frente -1
string = frase[::-1]
if frase == string:
    print(f'{frase} é um palíndromo')
else:
    print(f'{frase} não é um palíndromo')



