numero = int(input('Digite um número entre 1000 e 9999: '))

while numero < 1000 or numero > 9999:
    numero = int(input('Valor inválido! Digite um número entre 1000 e 9999: '))

print('Número válido: {}'.format(numero))

numero_caracter = str(numero) #converter para acessar

print('Unidade: {}'.format(numero_caracter [3]))
print('Dezena: {}'.format(numero_caracter [2]))
print('Centena: {}'.format(numero_caracter [1]))
print('Milhar: {}'.format(numero_caracter [0]))