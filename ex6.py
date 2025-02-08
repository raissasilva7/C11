import math

numero = float(input("Digite um número: "))

raiz = math.sqrt(numero)  # Raiz quadrada
teto = math.ceil(numero)  # Função teto (arredonda para cima)
chao = math.floor(numero)  # Função chão (arredonda para baixo)
parte_inteira = int(numero)  # Remove a parte decimal

print('Número digitado: {}'.format(numero))
print('Raiz quadrada: {}'.format(raiz))
print('Função teto: {}'.format(teto))
print('Função chão: {}'.format(chao))
print('Parte inteira: {}'.format(parte_inteira))
