print('=' * 11, 'LOJÃO REAL', '=' * 11)
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTOS:
[ 1 ] á vista  no dinheiro/cheque
[ 2 ] á vista no cartão
[ 3 ] 2X no cartão
[ 4 ] 3X ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    print(f'Sua compra de R${preço:.2f} vai custar R${preço-(preço*10/100):.2f} no final.')
elif opção == 2:
    print(f'Sua compra de R${preço:.2f} vai custar R${preço-(preço*5/100):.2f} no final.')
elif opção == 3:
    print(f'sua compra de R${preço:.2f} vai custar R${preço:.2f} no final.')
elif opção == 4:
    parcela = int(input('Quantas parcelas? '))
    nvalor = preço + (preço*20/100)
    print(f'Sua compra será parcelada em {parcela}X de R${nvalor/parcela:.2f} com jurus')
    print(f'Sua compra de R${preço:.2f} vai custa R${nvalor:.2f} no final.')
else:
    print('Opção invalida de pagamento. Tente novamente!')
