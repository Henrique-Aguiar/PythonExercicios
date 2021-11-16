from datetime import date
ano = int(input('Ano de nacimento: '))
atual = date.today().year
idade = atual - ano
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('CLASSIFICAÇÃO: MIRIM')
elif 14 >= idade > 9:
    print('CLASSIFICAÇÃO: INFANTIL')
elif 19 >= idade > 14:
    print('CLASSIFICAÇÃO: JUNIOR')
elif 25 >= idade > 19:
    print('CLASSIFICAÇÃO: SÊNIOR')
elif idade > 25:
    print('CLASSIFICAÇÃO: MASTER')
