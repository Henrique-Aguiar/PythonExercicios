valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
mensal = valor / (anos*12)
print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos a prestação será de R${mensal:.2f}')
if mensal >= 30/100 * salario:
    print('Empréstimo negado! ')
else:
    print('Empréstimo pode ser concedido! ')
