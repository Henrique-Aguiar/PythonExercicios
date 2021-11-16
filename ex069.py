print('-'*30)
print('CADASTRE uma PESSOA')
print('-'*30)
total = mulher = men = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-'*30)
    if idade >= 18:
        total += 1
    if sexo == 'M':
        men += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
    print('-'*30)
print(f'Total de pessoas com mais de 18 anos: {total}')
print(f'Ao todo temos {men} homens cadastrados')
print(f'E temos {mulher} mulheres com menos de 20 anos')
