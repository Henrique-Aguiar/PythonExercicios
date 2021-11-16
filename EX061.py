print(f'{"=" * 30} \n'
      f'    10 TERMOS DE UMA PA\n'
      f'{"=" * 30}')
n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão: '))
termo = n1
cont = 1
while cont <= 10:
      print(f'{termo} → ', end='')
      termo += n2
      cont += 1
print('FIM')