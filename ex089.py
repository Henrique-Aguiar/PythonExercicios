lista = []
while True:
   nome = str(input('Nome: '))
   nota1 = float(input('Nota 1: '))
   nota2 = float(input('nota 2: '))
   media = (nota1 + nota2) / 2
   lista.append([nome, [nota1, nota2], media])
   resp = str(input('Quer continuar? [S/N] '))
   if resp in 'Nn':
       break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-' * 26)
while True:
    n = int(input('Mostrar notas de qual aluno? (999 para interrompe): '))
    if n == 999:
        break
    else:
        print(f'Notas de {lista[n][0]} são {lista[n][1]}')
        print('-' * 26)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
