'''ano = int( input('Ano de nacimento: '))
idade = 2021 - ano
print(f'Quem naceu em {ano} tem {idade} anos em 2021.')
if idade > 18:
    print(f'Você já deveria ter se alistado há {idade-18} anos.')
    print(f'Seu alistamento foi em {ano+18}. ')
elif idade < 18:
    print(f'Ainda faltam {18-idade} anos para o alistamento')
    print(f'Seu alistamento será em {ano+18}')
else:
    print('Você tem que se alista imediatamente!')'''
from datetime import date
atual = date.today().year
ano = int( input('Ano de nacimento: '))
idade = atual - ano
print(f'Quem naceu em {ano} tem {idade} anos em {atual}.')
if idade > 18:
    print(f'Você já deveria ter se alistado há {idade - 18} anos.')
    print(f'Seu alistamento foi em {ano + 18}. ')
elif idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o alistamento')
    print(f'Seu alistamento será em {ano + 18}')
else:
    print('Você tem que se alistar imediatamente!')

