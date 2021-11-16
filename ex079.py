valores = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    '''op = ' '
    while op not in 'SN':'''
    while True:
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if op in 'SN':
            break
    if op == 'N':
        break
valores.sort()
print('-='*40)
print(f'Você digitou os valores {valores}')
