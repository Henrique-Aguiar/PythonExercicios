lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = ster = mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if lista[l][c] % 2 == 0:
            spar += lista[l][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]:^5}]', end='')
    ster += lista[l][2]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}.')
print(f'A soma dos valores da terceira coluna é {ster}.')
for c in range(0, 3):
    if c == 0:
        mai = lista[1][c]
    elif lista[1][c] > mai:
        mai = lista[1][c]
print(f'O maior da segunda linha é {mai}.')
