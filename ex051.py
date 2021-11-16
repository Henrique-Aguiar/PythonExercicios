print(f'{"=" * 30} \n'
      f'    10 TERMOS DE UMA PA\n'
      f'{"=" * 30}')
n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão: '))
décimo = n1 + (10 - 1) * n2
for c in range(n1, décimo + n2, n2):
    print(f'{c}', end=' → ')
print('Acabou')
