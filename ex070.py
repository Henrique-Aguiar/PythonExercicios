print('-'*30)
print('   LOJÃO REAL')
print('-'*30)
total = mil = menor = cont = 0
barato =' '
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    total += preço
    cont += 1
    if preço > 1000:
        mil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    '''else:
       if preço < menor:
            menor = preço
            barato = nome'''
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).upper()[0]
    if op == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
