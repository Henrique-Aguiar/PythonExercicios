def area(a, b):
    ar = a * b
    print(f'A área de um terreno {a}x{b} é de {ar}m²')


print(' CONTROLE DE TERRENOS')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
