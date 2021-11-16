número = (int(input('Digite um número: ')),
          int(input('Digite outro número: ')),
          int(input('Digite mais um número: ')),
          int(input('Digite o último número: ')))
print(f'Você digitou os valores {número}')
print(f'O valor 9 apareceu {número.count(9)} veezes')
if 3 in número:
    print(f'O valor 3 apareceu na {número.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in número:
    if n % 2 == 0:
        print(f'{n}', end=' ')
