numero = int(input('Digite um numero inteiro: '))
print('''Escolhar uma das bases para conversão: 
[ 1 ] converter para BINÁRIO')
[ 2 ] converter para OCTAL')
[ 3 ] converter para HEXADECIMAL''')
base = int(input('Sua posição: '))
if base == 1:
    print(f'{numero} convertido para BINÁRIO é igual a {bin(numero)[2:]}')
elif base == 2:
    print(f'{numero} convertido para OCTAL é igual a {oct(numero)[2:]}')
elif base == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}')
else:
    print('Opção inválida. Tente novamente.')
    