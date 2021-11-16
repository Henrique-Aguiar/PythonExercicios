n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O \033[31mPRIMEIRO\033[m valor é maior')
elif n2 > n1:
    print('O \033[31mSEGUNDO\033[m valor é maior ')
else:
    print('Não existe valor maior os dois são iguais')
