resp = 'S'
cont = soma = maior = menor = média = 0
while resp in 'S':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / cont
print(f'Você digitou {cont} números e a média foi {média:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')


