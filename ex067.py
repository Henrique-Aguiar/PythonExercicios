while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    print('-' * 20)
    for cont in range(1, 11):
        print(f'{num} x {cont} = {num*cont}')
    print('-'*20)
print('Progama tabuada encerrado. Volte sempre!')

