print(f'{"=" * 30} \n'
      f'    10 TERMOS DE UMA PA\n'
      f'{"=" * 30}')
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
      total += mais
      while cont <= total:
            print(f'{termo} → ', end='')
            termo += razão
            cont += 1
      print('PAUSA')
      mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')


