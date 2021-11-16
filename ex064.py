n = soma = total =0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    soma += n
    total += 1
    n = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {total} e a soma entre eles foi {soma}')

