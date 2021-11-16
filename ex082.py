num = []
par = []
imp = []
while True:
    num.append(int(input('Digite um número: ')))
    res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if res in 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    else:
        imp.append(v)
print('-='*30)
print(f'A lista completa é {num}')
print(f'A lista com pares é {par}')
print(f'A lista com ímpares é {imp}')
