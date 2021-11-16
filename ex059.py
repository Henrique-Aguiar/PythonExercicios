from time import sleep
opção = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar 
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do progama''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        print(f'A soma entre {n1} + {n2} é {n1 + n2}')
    elif opção == 2:
        print(f'O resultado de {n1} x {n2} é {n1*n2}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção != 5:
        print('Opção inválida. tente novamente ')
    print('=-='*10)
print('finalizando...')
sleep(2)
print('Fim do progama! Volte sempre!')
