s = float(input('Qual é o salario do funcionário? R$'))
if s > 1250:
    sa = s + (s * 10 / 100)
else:
    sa = s + (s * 15 / 100)
print(f'Quem ganha R${s:.2f} passa a ganhar R${sa:.2f}  ')
