
temperatura = [12, 11, 20, 21, 2, 45, 10]
dias_week = ['D', 'S', 'T', 'Q', 'Q', 'S', 'S']

for temperatura, dia in zip(temperatura, dias_week):
    barra_temperatura = '*' * temperatura
    print(f'{dia}: {barra_temperatura}')