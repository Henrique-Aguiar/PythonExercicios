listagem = ('Lápis', 0.5,
            'Borracha', 1.5,
            'Caderno', 18,
            'Estojo', 25,
            'Compasso', 5,
            'Mochila', 99.99,
            'Canetas', 3,
            'Livros', 47.80)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>6.2f}')
print('-'*40)
