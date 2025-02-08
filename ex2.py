numero = int(input('Qual numero para fazer a tabuada? '))
inicio = int(input('Qual intervalo de inicio? '))
fim = int(input('Qual intervalo de fim? '))
print('O numero é {} com intervalo de {} a {}'.format(numero, inicio, fim))

for c in range(inicio, fim +1):
    resultado = numero * c
    print('{} x {} = {}'.format(numero,c,resultado))