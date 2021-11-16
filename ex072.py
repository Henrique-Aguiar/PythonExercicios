cont = ('zero', 'um', 'dois', 'três', 'quatro',
          'cinco', 'seis', 'sete', 'oito', 'nove',
          'dez', 'onze', 'doze', 'treze', 'catorze',
          'quize', 'dezesseis', 'dezessete', 'dezoito',
          'dezenove', 'vinte')
while True:
    while True:
        núm = int(input('Digite um número entre 0 e 20: '))
        if 0 <= núm <= 20:
            break
        print('Tente novamente.', end=' ')
    print(f'Você digitou o número {cont[núm]}')
    opç = ' '
    while opç not in 'SN':
        opç = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opç == 'N':
        break
print('FIM')



