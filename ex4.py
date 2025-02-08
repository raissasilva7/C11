distancia = float(input('Qual distancia da viagem em Km?'))
if distancia <= 200:
    r = distancia * 0.50
    print('Passagem é R$ {}'.format(r))
else:
    r = distancia * 0.45
    print('Passagem é R$ {}'.format(r))