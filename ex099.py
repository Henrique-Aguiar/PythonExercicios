from time import sleep


def maior(* núm):
    print('-=' * 30)
    cont = maior = 0
    print('Analizando os valores passados...')
    for valor in núm:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram imformados {cont} valores ao todo.')
    print(f'O mair valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()