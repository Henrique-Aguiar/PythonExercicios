from datetime import datetime
info = {}
info['nome'] = str(input('Nome: '))
ano = int(input('Ano de nacimento: '))
info['idade'] = datetime.now().year - ano
info['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if info['ctps'] != 0:
    info['contratação'] = int(input('Ano de Contratação: '))
    info['salário'] = float(input('Salário: R$'))
    info['aposentadoria'] = info['idade'] + ((info['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in info.items():
    print(f' - {k} tem o valor {v}')